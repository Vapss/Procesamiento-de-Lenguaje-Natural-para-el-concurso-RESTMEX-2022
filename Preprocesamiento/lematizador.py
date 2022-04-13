#~ import freeling
from Preprocesamiento.utilidades import pyfreeling
import sys, re
import os

## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

## Check whether we know where to find FreeLing data files
if "FREELINGDIR" not in os.environ :
   if sys.platform == "win32" or sys.platform == "win64" : os.environ["FREELINGDIR"] = "C:\\Program Files"
   else : os.environ["FREELINGDIR"] = "/usr"
   print("FREELINGDIR environment variable not defined, trying ", os.environ["FREELINGDIR"], file=sys.stderr)

if not os.path.exists(os.environ["FREELINGDIR"]+"/share/freeling") :
   print("Folder",os.environ["FREELINGDIR"]+"/share/freeling",
         "not found.\nPlease set FREELINGDIR environment variable to FreeLing installation directory",
         file=sys.stderr)
   sys.exit(1)


# Location of FreeLing configuration files.
DATA = os.environ["FREELINGDIR"]+"/share/freeling/";

# Init locales
pyfreeling.util_init_locale("default");

# create language detector. Used just to show it. Results are printed
# but ignored (after, it is assumed language is LANG)
la=pyfreeling.lang_ident(DATA+"common/lang_ident/ident-few.dat");

# create options set for maco analyzer. Default values are Ok, except for data files.
LANG="es";
op= pyfreeling.maco_options(LANG);
op.set_data_files( "", 
                   DATA + "common/punct.dat",
                   DATA + LANG + "/dicc.src",
                   DATA + LANG + "/afixos.dat",
                   "",
                   DATA + LANG + "/locucions.dat", 
                   DATA + LANG + "/np.dat",
                   DATA + LANG + "/quantities.dat",
                   DATA + LANG + "/probabilitats.dat");

# create analyzers
tk=pyfreeling.tokenizer(DATA+LANG+"/tokenizer.dat");
sp=pyfreeling.splitter(DATA+LANG+"/splitter.dat");
sid=sp.open_session();
mf=pyfreeling.maco(op);

# activate mmorpho odules to be used in next call
mf.set_active_options(False, True, True, True,  # select which among created 
                      True, True, False, True,  # submodules are to be used. 
                      True, True, True, True ); # default: all created submodules are used

# create tagger, sense anotator, and parsers
tg=pyfreeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
sen=pyfreeling.senses(DATA+LANG+"/senses.dat");
parser= pyfreeling.chart_parser(DATA+LANG+"/chunker/grammar-chunk.dat");
dep=pyfreeling.dep_txala(DATA+LANG+"/dep_txala/dependences.dat", parser.get_start_symbol());

def lematizar(linea):
	
	punto_agregado = False
	if not re.search(r"[\.$]",linea):
		linea = linea + "."
		punto_agregado = True
	
	palabras = tk.tokenize(linea)
	ls = sp.split(sid,palabras,False)
	ls = mf.analyze(ls)
	resultado = ''
	for s in ls :
		ws = s.get_words()
		for w in ws :
			resultado += w.get_lemma() + ' '
			#~ resultado += w.get_form() + ' '
			#w.get_form()+" "+w.get_lemma()+" "+w.get_tag()
	resultado = re.sub('\s+', ' ', resultado)
	if punto_agregado:
		resultado = re.sub('\.', '', resultado)
	
	return (resultado)
	
