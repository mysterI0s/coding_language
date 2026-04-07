grammar alexer;
program : statement* EOF ;
statement
    : varDecl
    | exprStmt
    ;
varDecl : VAR ID COLON type ASSIGN expr SEMI ;
exprStmt : expr SEMI ;
type : INT_T | FLOAT_T ;

expr
    : LPAREN expr RPAREN
    | expr (MUL | DIV) expr          
    | expr (PLUS | MINUS) expr       
    | NUMBER                         
    | ID                             
    ;


VAR     : 'متغير' ;
IF      : 'إذا' ;
ELSE    : 'وإال' ;
WHILE   : 'بينما' ;
PRINT   : 'اظهر' ;
TRUE    : 'صح' ;
FALSE   : 'خاطئ' ;
INT_T   : 'صحيح' ;
FLOAT_T : 'عشري' ;
READ    : 'اقرأ' ;

ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
GT      : '>' ;
LT      : '<' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
COLON   : ':' ;
SEMI    : 'الفاصلة المنقوطة العربية' ;

//Numbers

fragment DIGIT : [0-9] | [\u0660-\u0669] ;
NUMBER  : DIGIT+ ('.' DIGIT+)? ;

//Identifiers
ID      : [\u0621-\u064A] [\u0621-\u064A\u0660-\u06690-9_]* ;

//Whitespace and Comments
WS      : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;


/// Parser Rules (for testing purposes)

