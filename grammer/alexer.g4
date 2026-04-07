lexer grammar alexer;
VAR     : 'متغير' ;
IF      : 'إذا' ;
ELSE    : 'وإال' ;
WHILE   : 'طالما' ;
PRINT   : 'اطبع' ;
TRUE    : 'صح' ;
FALSE   : 'خطأ' ;
INT_T   : 'صحيح' ;
FLOAT_T : 'عشري' ;

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
