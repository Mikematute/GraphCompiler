
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ARC BOOL CHAR COLON COMA CTE_BOO CTE_CHAR CTE_FLO CTE_INT CTE_STRING DEG DELETE DIAMETER DIRECTED DIV DO DOT ELSE EQL EQUALTO FLOAT FOR ID IF IN INT LBRACK LCORCH LESSEQUAL LESST LPAREN MAIN MOREEQUAL MORET MUL NODE NOT NOTEQUALTO OR PRINT PROGRAM RBRACK RCORCH RESD RPAREN SCOLO SHORTPATH STRING SUB SUMA UNDIRECTED VAR VOID WHILEprogram : PROGRAM ID SCOLO vars function bodyvars : VAR type vars_1 SCOLO vars\n            | emptyvars_1 : ID vars_2\n              | ID vars_2 COMA vars_1vars_2 : array_declare\n              | emptyfunction : function_t ID LPAREN function_v RPAREN LBRACK vars statutes RBRACK function\n                | emptyfunction_t : VOID\n                  | t_number\n                  | t_string\n                  | t_bool\n                  | t_graphfunction_v : function_v1\n                  | emptyfunction_v1 : type ID\n                   | type ID COMA function_v1\n                   | type ID array_declare\n                   | type ID array_declare COMA function_v1body : MAIN LPAREN RPAREN LBRACK vars statutes RBRACKtype : t_number\n            | t_string\n            | t_bool\n            | t_grapht_number : INT\n                | FLOATt_string : STRING\n                | CHARt_bool : BOOLt_graph : NODE\n               | ARC\n               | UNDIRECTED\n               | DIRECTEDarray_declare : LCORCH CTE_INT RCORCH array_declare_1array_declare_1 : LCORCH CTE_INT RCORCH array_declare_1\n                       | emptystatutes : statutes_1 statutes\n                | emptystatutes_1 : assignation\n                  | writing\n                  | condition\n                  | cycle\n                  | function_callassignation : ID EQL expressionwriting : PRINT LPAREN writing_1 RPAREN SCOLOwriting_1 : expression\n                 | CTE_STRING\n                 | writing_2writing_2 : expression SUMA writing_1\n                 | CTE_STRING SUMA writing_1condition : IF LPAREN expression RPAREN LBRACK statutes RBRACK condition_1 SCOLOcondition_1 : ELSE LBRACK expression RBRACK\n                   | emptycycle : c_while\n             | c_do\n             | c_for\n             | c_forinc_while : WHILE LPAREN expression RPAREN LBRACK statutes RBRACKc_do : DO LBRACK statutes RBRACK WHILE LPAREN expression RPARENc_for : FOR LPAREN ID SCOLO expression SCOLO assignation RPAREN LBRACK statutes RBRACKc_forin : FOR LPAREN ID IN ID RPAREN LBRACK statutes RBRACKfunction_call : ID LPAREN function_call_1 RPAREN SCOLOfunction_call_1 : function_call_2\n                       | emptyfunction_call_2 : expression\n                       | ID\n                       | expression SCOLO function_call_2\n                       | ID SCOLO function_call_2expression : exp_lv1\n                  | exp_lv1 AND expression\n                  | exp_lv1 OR expressionexp_lv1 : exp_lv2 exp_lv1_1exp_lv1_1 : LESST exp_lv2\n                 | MORET exp_lv2\n                 | LESSEQUAL exp_lv2\n                 | MOREEQUAL exp_lv2\n                 | EQUALTO exp_lv2\n                 | NOTEQUALTO exp_lv2\n                 | emptyexp_lv2 : exp_lv3\n               | exp_lv3 SUMA exp_lv2\n               | exp_lv3 SUB exp_lv2exp_lv3 : exp_lv4\n               | exp_lv4 MUL exp_lv3\n               | exp_lv4 DIV exp_lv3\n               | exp_lv4 RESD exp_lv3exp_lv4 : exp_lv5\n               | NOT exp_lv5exp_lv5 : RPAREN expression LPAREN\n               | var_cte\n               | method\n               | ID\n               | ID array_accessarray_access : LCORCH arrary_access_1 RCORCH arrary_access_2arrary_access_1 : CTE_INT\n                       | IDarrary_access_2 : LCORCH arrary_access_1 RCORCH arrary_access_2\n                       | emptyvar_cte : CTE_INT\n               | CTE_FLO\n               | CTE_BOO\n               | CTE_STRING\n               | CTE_CHARmethod : ID DOT method_t LPAREN method_1 RPARENmethod_1 : method_1_1\n                | emptymethod_1_1 : method_v\n                  | method_v COMA method_1_1method_t : DEG\n                | SHORTPATH\n                | DIAMETER\n                | ADD\n                | DELETE\n                | ARCmethod_v : ID\n                | LBRACK ID COMA ID RBRACKempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,30,84,],[0,-1,-21,]),'ID':([2,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,37,46,47,48,50,55,56,63,65,66,67,68,69,73,74,75,76,80,86,87,88,89,90,91,92,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,127,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,157,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,194,195,198,199,206,207,208,209,211,215,216,217,223,227,228,229,230,231,232,234,239,],[3,-3,32,-10,-11,-12,-13,-14,-26,-27,-28,-29,-30,-31,-32,-33,-34,34,-22,-23,-24,-25,-118,52,-2,34,-118,70,-118,70,-40,-41,-42,-43,-44,-55,-56,-57,-58,70,96,112,96,96,96,70,124,-93,-45,-70,-118,-81,-84,-88,96,96,-91,-92,-100,-101,-102,-103,-104,-94,168,96,96,-73,96,96,96,96,96,96,-80,96,96,96,96,96,-89,112,112,96,96,96,193,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,70,70,201,-118,96,213,218,168,-95,-99,-59,70,-105,201,-60,233,-118,-52,96,70,-62,-98,-61,]),'SCOLO':([3,33,34,38,39,40,53,54,60,61,95,96,98,99,100,101,102,105,106,107,108,109,110,111,112,116,124,126,127,132,139,145,148,150,169,170,171,172,173,174,175,176,177,178,179,180,181,182,192,195,208,209,210,216,220,222,228,234,238,],[4,37,-118,-4,-6,-7,-5,-118,-35,-37,-118,-93,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,147,149,156,-36,-94,-73,-80,-89,184,186,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,199,-118,-95,-99,-118,-105,229,-54,-118,-98,-53,]),'VAR':([4,37,50,56,],[6,6,6,6,]),'VOID':([4,5,7,37,47,125,],[-118,11,-3,-118,-2,11,]),'INT':([4,5,6,7,36,37,47,57,82,125,],[-118,16,16,-3,16,-118,-2,16,16,16,]),'FLOAT':([4,5,6,7,36,37,47,57,82,125,],[-118,17,17,-3,17,-118,-2,17,17,17,]),'STRING':([4,5,6,7,36,37,47,57,82,125,],[-118,18,18,-3,18,-118,-2,18,18,18,]),'CHAR':([4,5,6,7,36,37,47,57,82,125,],[-118,19,19,-3,19,-118,-2,19,19,19,]),'BOOL':([4,5,6,7,36,37,47,57,82,125,],[-118,20,20,-3,20,-118,-2,20,20,20,]),'NODE':([4,5,6,7,36,37,47,57,82,125,],[-118,21,21,-3,21,-118,-2,21,21,21,]),'ARC':([4,5,6,7,36,37,47,57,82,125,128,],[-118,22,22,-3,22,-118,-2,22,22,22,165,]),'UNDIRECTED':([4,5,6,7,36,37,47,57,82,125,],[-118,23,23,-3,23,-118,-2,23,23,23,]),'DIRECTED':([4,5,6,7,36,37,47,57,82,125,],[-118,24,24,-3,24,-118,-2,24,24,24,]),'MAIN':([4,5,7,8,10,37,47,125,158,],[-118,-118,-3,31,-9,-118,-2,-118,-8,]),'PRINT':([7,37,47,50,55,56,63,65,66,67,68,69,73,74,75,76,80,91,96,97,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,208,209,211,215,216,223,228,229,231,232,234,239,],[-3,-118,-2,-118,71,-118,71,-40,-41,-42,-43,-44,-55,-56,-57,-58,71,71,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,71,71,-118,-95,-99,-59,71,-105,-60,-118,-52,71,-62,-98,-61,]),'IF':([7,37,47,50,55,56,63,65,66,67,68,69,73,74,75,76,80,91,96,97,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,208,209,211,215,216,223,228,229,231,232,234,239,],[-3,-118,-2,-118,72,-118,72,-40,-41,-42,-43,-44,-55,-56,-57,-58,72,72,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,72,72,-118,-95,-99,-59,72,-105,-60,-118,-52,72,-62,-98,-61,]),'WHILE':([7,37,47,50,55,56,63,65,66,67,68,69,73,74,75,76,80,91,96,97,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,155,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,208,209,211,215,216,223,228,229,231,232,234,239,],[-3,-118,-2,-118,77,-118,77,-40,-41,-42,-43,-44,-55,-56,-57,-58,77,77,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,191,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,77,77,-118,-95,-99,-59,77,-105,-60,-118,-52,77,-62,-98,-61,]),'DO':([7,37,47,50,55,56,63,65,66,67,68,69,73,74,75,76,80,91,96,97,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,208,209,211,215,216,223,228,229,231,232,234,239,],[-3,-118,-2,-118,78,-118,78,-40,-41,-42,-43,-44,-55,-56,-57,-58,78,78,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,78,78,-118,-95,-99,-59,78,-105,-60,-118,-52,78,-62,-98,-61,]),'FOR':([7,37,47,50,55,56,63,65,66,67,68,69,73,74,75,76,80,91,96,97,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,208,209,211,215,216,223,228,229,231,232,234,239,],[-3,-118,-2,-118,79,-118,79,-40,-41,-42,-43,-44,-55,-56,-57,-58,79,79,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,79,79,-118,-95,-99,-59,79,-105,-60,-118,-52,79,-62,-98,-61,]),'RBRACK':([7,37,47,50,55,56,62,63,64,65,66,67,68,69,73,74,75,76,80,85,91,93,96,97,98,99,100,101,102,105,106,107,108,109,110,111,123,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,184,186,189,190,195,196,197,208,209,211,215,216,223,225,228,229,231,232,233,234,235,236,239,],[-3,-118,-2,-118,-118,-118,84,-118,-39,-40,-41,-42,-43,-44,-55,-56,-57,-58,-118,-38,-118,125,-93,-45,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,155,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-63,-46,-118,-118,-118,210,211,-95,-99,-59,-118,-105,-60,232,-118,-52,-118,-62,237,-98,238,239,-61,]),'LPAREN':([31,32,70,71,72,77,79,96,98,99,100,101,102,105,106,107,108,109,110,111,127,132,139,145,146,159,160,161,162,163,164,165,169,170,171,172,173,174,175,176,177,178,179,180,181,182,191,195,208,209,216,228,234,],[35,36,87,88,89,90,92,-93,-70,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-94,-73,-80,-89,182,194,-110,-111,-112,-113,-114,-115,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,198,-118,-95,-99,-105,-118,-98,]),'LCORCH':([34,52,54,95,96,112,195,228,],[41,41,59,59,129,129,207,207,]),'COMA':([34,38,39,40,52,54,58,60,61,95,126,201,205,218,237,],[-118,48,-6,-7,57,-118,82,-35,-37,-118,-36,-116,217,227,-117,]),'RPAREN':([35,36,43,44,45,52,54,58,60,61,81,86,87,88,89,90,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,126,127,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,147,149,151,152,156,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,185,187,188,193,194,195,198,201,202,203,204,205,208,209,212,214,216,226,228,230,234,237,],[42,-118,51,-15,-16,-17,-118,-19,-35,-37,-18,104,104,104,104,104,-20,-118,-93,-45,-70,-118,-81,-84,-88,104,104,-91,-92,-100,-101,-102,-103,-104,-67,148,-64,-65,-66,150,-47,-48,-49,153,154,-36,-94,104,104,-73,104,104,104,104,104,104,-80,104,104,104,104,104,-89,104,104,104,104,104,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-69,-68,-50,-51,200,-118,-118,104,-116,216,-106,-107,-108,-95,-99,223,224,-105,-109,-118,104,-98,-117,]),'CTE_INT':([41,59,86,87,88,89,90,103,104,129,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,207,230,],[49,83,107,107,107,107,107,107,107,167,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,167,107,]),'LBRACK':([42,51,78,153,154,194,200,217,221,224,],[50,56,91,189,190,206,215,206,230,231,]),'RCORCH':([49,83,166,167,168,219,],[54,95,195,-96,-97,228,]),'EQL':([70,213,],[86,86,]),'NOT':([86,87,88,89,90,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'CTE_FLO':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,108,]),'CTE_BOO':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,109,]),'CTE_STRING':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[110,110,119,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,110,119,119,110,110,110,]),'CTE_CHAR':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,111,]),'MUL':([96,101,102,105,106,107,108,109,110,111,112,119,127,145,182,195,208,209,216,228,234,],[-93,142,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-90,-118,-95,-99,-105,-118,-98,]),'DIV':([96,101,102,105,106,107,108,109,110,111,112,119,127,145,182,195,208,209,216,228,234,],[-93,143,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-90,-118,-95,-99,-105,-118,-98,]),'RESD':([96,101,102,105,106,107,108,109,110,111,112,119,127,145,182,195,208,209,216,228,234,],[-93,144,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-90,-118,-95,-99,-105,-118,-98,]),'SUMA':([96,98,99,100,101,102,105,106,107,108,109,110,111,112,118,119,127,132,139,145,169,170,171,172,173,174,175,176,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,-70,-118,140,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,151,152,-94,-73,-80,-89,-71,-72,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'SUB':([96,100,101,102,105,106,107,108,109,110,111,112,119,127,145,179,180,181,182,195,208,209,216,228,234,],[-93,141,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'LESST':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,133,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'MORET':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,134,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'LESSEQUAL':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,135,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'MOREEQUAL':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,136,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'EQUALTO':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,137,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'NOTEQUALTO':([96,99,100,101,102,105,106,107,108,109,110,111,112,119,127,145,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,138,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-89,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'AND':([96,98,99,100,101,102,105,106,107,108,109,110,111,112,119,127,132,139,145,171,172,173,174,175,176,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,130,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-73,-80,-89,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'OR':([96,98,99,100,101,102,105,106,107,108,109,110,111,112,119,127,132,139,145,171,172,173,174,175,176,177,178,179,180,181,182,195,208,209,216,228,234,],[-93,131,-118,-81,-84,-88,-91,-92,-100,-101,-102,-103,-104,-93,-103,-94,-73,-80,-89,-74,-75,-76,-77,-78,-79,-82,-83,-85,-86,-87,-90,-118,-95,-99,-105,-118,-98,]),'DOT':([96,112,],[128,128,]),'IN':([124,],[157,]),'DEG':([128,],[160,]),'SHORTPATH':([128,],[161,]),'DIAMETER':([128,],[162,]),'ADD':([128,],[163,]),'DELETE':([128,],[164,]),'ELSE':([210,],[221,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'vars':([4,37,50,56,],[5,47,55,80,]),'empty':([4,5,34,36,37,50,54,55,56,63,80,87,91,95,99,125,189,190,194,195,210,215,228,231,],[7,10,40,45,7,7,61,64,7,64,64,115,64,61,139,10,64,64,204,209,222,64,209,64,]),'function':([5,125,],[8,158,]),'function_t':([5,125,],[9,9,]),'t_number':([5,6,36,57,82,125,],[12,26,26,26,26,12,]),'t_string':([5,6,36,57,82,125,],[13,27,27,27,27,13,]),'t_bool':([5,6,36,57,82,125,],[14,28,28,28,28,14,]),'t_graph':([5,6,36,57,82,125,],[15,29,29,29,29,15,]),'type':([6,36,57,82,],[25,46,46,46,]),'body':([8,],[30,]),'vars_1':([25,48,],[33,53,]),'vars_2':([34,],[38,]),'array_declare':([34,52,],[39,58,]),'function_v':([36,],[43,]),'function_v1':([36,57,82,],[44,81,94,]),'array_declare_1':([54,95,],[60,126,]),'statutes':([55,63,80,91,189,190,215,231,],[62,85,93,123,196,197,225,236,]),'statutes_1':([55,63,80,91,189,190,215,231,],[63,63,63,63,63,63,63,63,]),'assignation':([55,63,80,91,189,190,199,215,231,],[65,65,65,65,65,65,214,65,65,]),'writing':([55,63,80,91,189,190,215,231,],[66,66,66,66,66,66,66,66,]),'condition':([55,63,80,91,189,190,215,231,],[67,67,67,67,67,67,67,67,]),'cycle':([55,63,80,91,189,190,215,231,],[68,68,68,68,68,68,68,68,]),'function_call':([55,63,80,91,189,190,215,231,],[69,69,69,69,69,69,69,69,]),'c_while':([55,63,80,91,189,190,215,231,],[73,73,73,73,73,73,73,73,]),'c_do':([55,63,80,91,189,190,215,231,],[74,74,74,74,74,74,74,74,]),'c_for':([55,63,80,91,189,190,215,231,],[75,75,75,75,75,75,75,75,]),'c_forin':([55,63,80,91,189,190,215,231,],[76,76,76,76,76,76,76,76,]),'expression':([86,87,88,89,90,104,130,131,147,149,151,152,156,198,230,],[97,116,118,121,122,146,169,170,116,116,118,118,192,212,235,]),'exp_lv1':([86,87,88,89,90,104,130,131,147,149,151,152,156,198,230,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,]),'exp_lv2':([86,87,88,89,90,104,130,131,133,134,135,136,137,138,140,141,147,149,151,152,156,198,230,],[99,99,99,99,99,99,99,99,171,172,173,174,175,176,177,178,99,99,99,99,99,99,99,]),'exp_lv3':([86,87,88,89,90,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,179,180,181,100,100,100,100,100,100,100,]),'exp_lv4':([86,87,88,89,90,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,101,]),'exp_lv5':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[102,102,102,102,102,145,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,102,]),'var_cte':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'method':([86,87,88,89,90,103,104,130,131,133,134,135,136,137,138,140,141,142,143,144,147,149,151,152,156,198,230,],[106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,106,]),'function_call_1':([87,],[113,]),'function_call_2':([87,147,149,],[114,183,185,]),'writing_1':([88,151,152,],[117,187,188,]),'writing_2':([88,151,152,],[120,120,120,]),'array_access':([96,112,],[127,127,]),'exp_lv1_1':([99,],[132,]),'method_t':([128,],[159,]),'arrary_access_1':([129,207,],[166,219,]),'method_1':([194,],[202,]),'method_1_1':([194,217,],[203,226,]),'method_v':([194,217,],[205,205,]),'arrary_access_2':([195,228,],[208,234,]),'condition_1':([210,],[220,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SCOLO vars function body','program',6,'p_program','yacc_c.py',137),
  ('vars -> VAR type vars_1 SCOLO vars','vars',5,'p_vars','yacc_c.py',141),
  ('vars -> empty','vars',1,'p_vars','yacc_c.py',142),
  ('vars_1 -> ID vars_2','vars_1',2,'p_vars_1','yacc_c.py',149),
  ('vars_1 -> ID vars_2 COMA vars_1','vars_1',4,'p_vars_1','yacc_c.py',150),
  ('vars_2 -> array_declare','vars_2',1,'p_vars_2','yacc_c.py',157),
  ('vars_2 -> empty','vars_2',1,'p_vars_2','yacc_c.py',158),
  ('function -> function_t ID LPAREN function_v RPAREN LBRACK vars statutes RBRACK function','function',10,'p_function','yacc_c.py',162),
  ('function -> empty','function',1,'p_function','yacc_c.py',163),
  ('function_t -> VOID','function_t',1,'p_function_t','yacc_c.py',167),
  ('function_t -> t_number','function_t',1,'p_function_t','yacc_c.py',168),
  ('function_t -> t_string','function_t',1,'p_function_t','yacc_c.py',169),
  ('function_t -> t_bool','function_t',1,'p_function_t','yacc_c.py',170),
  ('function_t -> t_graph','function_t',1,'p_function_t','yacc_c.py',171),
  ('function_v -> function_v1','function_v',1,'p_function_v','yacc_c.py',174),
  ('function_v -> empty','function_v',1,'p_function_v','yacc_c.py',175),
  ('function_v1 -> type ID','function_v1',2,'p_function_v1','yacc_c.py',178),
  ('function_v1 -> type ID COMA function_v1','function_v1',4,'p_function_v1','yacc_c.py',179),
  ('function_v1 -> type ID array_declare','function_v1',3,'p_function_v1','yacc_c.py',180),
  ('function_v1 -> type ID array_declare COMA function_v1','function_v1',5,'p_function_v1','yacc_c.py',181),
  ('body -> MAIN LPAREN RPAREN LBRACK vars statutes RBRACK','body',7,'p_body','yacc_c.py',184),
  ('type -> t_number','type',1,'p_type','yacc_c.py',187),
  ('type -> t_string','type',1,'p_type','yacc_c.py',188),
  ('type -> t_bool','type',1,'p_type','yacc_c.py',189),
  ('type -> t_graph','type',1,'p_type','yacc_c.py',190),
  ('t_number -> INT','t_number',1,'p_t_number','yacc_c.py',193),
  ('t_number -> FLOAT','t_number',1,'p_t_number','yacc_c.py',194),
  ('t_string -> STRING','t_string',1,'p_t_string','yacc_c.py',197),
  ('t_string -> CHAR','t_string',1,'p_t_string','yacc_c.py',198),
  ('t_bool -> BOOL','t_bool',1,'p_t_bool','yacc_c.py',201),
  ('t_graph -> NODE','t_graph',1,'p_t_graph','yacc_c.py',204),
  ('t_graph -> ARC','t_graph',1,'p_t_graph','yacc_c.py',205),
  ('t_graph -> UNDIRECTED','t_graph',1,'p_t_graph','yacc_c.py',206),
  ('t_graph -> DIRECTED','t_graph',1,'p_t_graph','yacc_c.py',207),
  ('array_declare -> LCORCH CTE_INT RCORCH array_declare_1','array_declare',4,'p_array_declare','yacc_c.py',210),
  ('array_declare_1 -> LCORCH CTE_INT RCORCH array_declare_1','array_declare_1',4,'p_array_declare_1','yacc_c.py',213),
  ('array_declare_1 -> empty','array_declare_1',1,'p_array_declare_1','yacc_c.py',214),
  ('statutes -> statutes_1 statutes','statutes',2,'p_statutes','yacc_c.py',217),
  ('statutes -> empty','statutes',1,'p_statutes','yacc_c.py',218),
  ('statutes_1 -> assignation','statutes_1',1,'p_statutes_1','yacc_c.py',221),
  ('statutes_1 -> writing','statutes_1',1,'p_statutes_1','yacc_c.py',222),
  ('statutes_1 -> condition','statutes_1',1,'p_statutes_1','yacc_c.py',223),
  ('statutes_1 -> cycle','statutes_1',1,'p_statutes_1','yacc_c.py',224),
  ('statutes_1 -> function_call','statutes_1',1,'p_statutes_1','yacc_c.py',225),
  ('assignation -> ID EQL expression','assignation',3,'p_assignation','yacc_c.py',228),
  ('writing -> PRINT LPAREN writing_1 RPAREN SCOLO','writing',5,'p_writing','yacc_c.py',231),
  ('writing_1 -> expression','writing_1',1,'p_writing_1','yacc_c.py',234),
  ('writing_1 -> CTE_STRING','writing_1',1,'p_writing_1','yacc_c.py',235),
  ('writing_1 -> writing_2','writing_1',1,'p_writing_1','yacc_c.py',236),
  ('writing_2 -> expression SUMA writing_1','writing_2',3,'p_writing_2','yacc_c.py',239),
  ('writing_2 -> CTE_STRING SUMA writing_1','writing_2',3,'p_writing_2','yacc_c.py',240),
  ('condition -> IF LPAREN expression RPAREN LBRACK statutes RBRACK condition_1 SCOLO','condition',9,'p_condition','yacc_c.py',243),
  ('condition_1 -> ELSE LBRACK expression RBRACK','condition_1',4,'p_condition_1','yacc_c.py',246),
  ('condition_1 -> empty','condition_1',1,'p_condition_1','yacc_c.py',247),
  ('cycle -> c_while','cycle',1,'p_cycle','yacc_c.py',250),
  ('cycle -> c_do','cycle',1,'p_cycle','yacc_c.py',251),
  ('cycle -> c_for','cycle',1,'p_cycle','yacc_c.py',252),
  ('cycle -> c_forin','cycle',1,'p_cycle','yacc_c.py',253),
  ('c_while -> WHILE LPAREN expression RPAREN LBRACK statutes RBRACK','c_while',7,'p_c_while','yacc_c.py',256),
  ('c_do -> DO LBRACK statutes RBRACK WHILE LPAREN expression RPAREN','c_do',8,'p_c_do','yacc_c.py',259),
  ('c_for -> FOR LPAREN ID SCOLO expression SCOLO assignation RPAREN LBRACK statutes RBRACK','c_for',11,'p_c_for','yacc_c.py',262),
  ('c_forin -> FOR LPAREN ID IN ID RPAREN LBRACK statutes RBRACK','c_forin',9,'p_c_forin','yacc_c.py',265),
  ('function_call -> ID LPAREN function_call_1 RPAREN SCOLO','function_call',5,'p_function_call','yacc_c.py',268),
  ('function_call_1 -> function_call_2','function_call_1',1,'p_function_call_1','yacc_c.py',271),
  ('function_call_1 -> empty','function_call_1',1,'p_function_call_1','yacc_c.py',272),
  ('function_call_2 -> expression','function_call_2',1,'p_function_call_2','yacc_c.py',275),
  ('function_call_2 -> ID','function_call_2',1,'p_function_call_2','yacc_c.py',276),
  ('function_call_2 -> expression SCOLO function_call_2','function_call_2',3,'p_function_call_2','yacc_c.py',277),
  ('function_call_2 -> ID SCOLO function_call_2','function_call_2',3,'p_function_call_2','yacc_c.py',278),
  ('expression -> exp_lv1','expression',1,'p_expression','yacc_c.py',282),
  ('expression -> exp_lv1 AND expression','expression',3,'p_expression','yacc_c.py',283),
  ('expression -> exp_lv1 OR expression','expression',3,'p_expression','yacc_c.py',284),
  ('exp_lv1 -> exp_lv2 exp_lv1_1','exp_lv1',2,'p_exp_lv1','yacc_c.py',287),
  ('exp_lv1_1 -> LESST exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',289),
  ('exp_lv1_1 -> MORET exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',290),
  ('exp_lv1_1 -> LESSEQUAL exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',291),
  ('exp_lv1_1 -> MOREEQUAL exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',292),
  ('exp_lv1_1 -> EQUALTO exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',293),
  ('exp_lv1_1 -> NOTEQUALTO exp_lv2','exp_lv1_1',2,'p_exp_lv1_1','yacc_c.py',294),
  ('exp_lv1_1 -> empty','exp_lv1_1',1,'p_exp_lv1_1','yacc_c.py',295),
  ('exp_lv2 -> exp_lv3','exp_lv2',1,'p_exp_lv2','yacc_c.py',298),
  ('exp_lv2 -> exp_lv3 SUMA exp_lv2','exp_lv2',3,'p_exp_lv2','yacc_c.py',299),
  ('exp_lv2 -> exp_lv3 SUB exp_lv2','exp_lv2',3,'p_exp_lv2','yacc_c.py',300),
  ('exp_lv3 -> exp_lv4','exp_lv3',1,'p_exp_lv3','yacc_c.py',303),
  ('exp_lv3 -> exp_lv4 MUL exp_lv3','exp_lv3',3,'p_exp_lv3','yacc_c.py',304),
  ('exp_lv3 -> exp_lv4 DIV exp_lv3','exp_lv3',3,'p_exp_lv3','yacc_c.py',305),
  ('exp_lv3 -> exp_lv4 RESD exp_lv3','exp_lv3',3,'p_exp_lv3','yacc_c.py',306),
  ('exp_lv4 -> exp_lv5','exp_lv4',1,'p_exp_lv4','yacc_c.py',309),
  ('exp_lv4 -> NOT exp_lv5','exp_lv4',2,'p_exp_lv4','yacc_c.py',310),
  ('exp_lv5 -> RPAREN expression LPAREN','exp_lv5',3,'p_exp_lv5','yacc_c.py',313),
  ('exp_lv5 -> var_cte','exp_lv5',1,'p_exp_lv5','yacc_c.py',314),
  ('exp_lv5 -> method','exp_lv5',1,'p_exp_lv5','yacc_c.py',315),
  ('exp_lv5 -> ID','exp_lv5',1,'p_exp_lv5','yacc_c.py',316),
  ('exp_lv5 -> ID array_access','exp_lv5',2,'p_exp_lv5','yacc_c.py',317),
  ('array_access -> LCORCH arrary_access_1 RCORCH arrary_access_2','array_access',4,'p_array_access','yacc_c.py',320),
  ('arrary_access_1 -> CTE_INT','arrary_access_1',1,'p_array_access_1','yacc_c.py',323),
  ('arrary_access_1 -> ID','arrary_access_1',1,'p_array_access_1','yacc_c.py',324),
  ('arrary_access_2 -> LCORCH arrary_access_1 RCORCH arrary_access_2','arrary_access_2',4,'p_array_access_2','yacc_c.py',327),
  ('arrary_access_2 -> empty','arrary_access_2',1,'p_array_access_2','yacc_c.py',328),
  ('var_cte -> CTE_INT','var_cte',1,'p_var_cte','yacc_c.py',331),
  ('var_cte -> CTE_FLO','var_cte',1,'p_var_cte','yacc_c.py',332),
  ('var_cte -> CTE_BOO','var_cte',1,'p_var_cte','yacc_c.py',333),
  ('var_cte -> CTE_STRING','var_cte',1,'p_var_cte','yacc_c.py',334),
  ('var_cte -> CTE_CHAR','var_cte',1,'p_var_cte','yacc_c.py',335),
  ('method -> ID DOT method_t LPAREN method_1 RPAREN','method',6,'p_method','yacc_c.py',339),
  ('method_1 -> method_1_1','method_1',1,'p_method_1','yacc_c.py',342),
  ('method_1 -> empty','method_1',1,'p_method_1','yacc_c.py',343),
  ('method_1_1 -> method_v','method_1_1',1,'p_method_1_1','yacc_c.py',346),
  ('method_1_1 -> method_v COMA method_1_1','method_1_1',3,'p_method_1_1','yacc_c.py',347),
  ('method_t -> DEG','method_t',1,'p_method_t','yacc_c.py',350),
  ('method_t -> SHORTPATH','method_t',1,'p_method_t','yacc_c.py',351),
  ('method_t -> DIAMETER','method_t',1,'p_method_t','yacc_c.py',352),
  ('method_t -> ADD','method_t',1,'p_method_t','yacc_c.py',353),
  ('method_t -> DELETE','method_t',1,'p_method_t','yacc_c.py',354),
  ('method_t -> ARC','method_t',1,'p_method_t','yacc_c.py',355),
  ('method_v -> ID','method_v',1,'p_method_v','yacc_c.py',358),
  ('method_v -> LBRACK ID COMA ID RBRACK','method_v',5,'p_method_v','yacc_c.py',359),
  ('empty -> <empty>','empty',0,'p_empty','yacc_c.py',363),
]
