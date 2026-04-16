// grammar alexer;
// program : statement* EOF ;
// statement
//     : varDecl
//     | assignStmt
//     | printStmt
//     | ifStmt
//     | whileStmt
//     | exprStmt
//     ;
// block : LBRACE statement* RBRACE ;
// varDecl    : VAR ID COLON type ASSIGN expr SEMI ;
// assignStmt : ID ASSIGN expr SEMI ;
// printStmt  : PRINT LPAREN expr RPAREN SEMI ;
// ifStmt : IF LPAREN expr RPAREN block (ELSE block)? ;
// whileStmt : WHILE LPAREN expr RPAREN block ;
// exprStmt : expr SEMI ;
// type : INT_T | FLOAT_T ;

// expr
// : LPAREN expr RPAREN
// | expr (MUL | DIV) expr
// | expr (PLUS | MINUS) expr
// | expr (GT | LT | '==' | '!=') expr   // عمليات المقارنة
// | NUMBER
// | ID
// ;


// VAR     : 'متغير' ;
// IF      : 'إذا' ;
// ELSE    : 'وإال' ;
// WHILE   : 'طالما' ;
// PRINT   : 'اطبع' ;
// INT_T   : 'صحيح' ;
// FLOAT_T : 'عشري' ;
// ASSIGN  : '=' ;
// PLUS    : '+' ;
// MINUS   : '-' ;
// MUL     : '*' ;
// DIV     : '/' ;
// GT      : '>' ;
// LT      : '<' ;
// LPAREN  : '(' ;
// RPAREN  : ')' ;
// LBRACE  : '{' ;
// RBRACE  : '}' ;
// COLON   : ':' ;
// SEMI    : '؛' ;

// //Numbers

// fragment DIGIT : [0-9] | [\u0660-\u0669] ;
// NUMBER  : DIGIT+ ('.' DIGIT+)? ;

// //Identifiers
// ID      : [\u0621-\u064A] [\u0621-\u064A\u0660-\u06690-9_]* ;


// //Whitespace and Comments
// WS      : [ \t\r\n]+ -> skip ;
// LINE_COMMENT : '//' ~[\r\n]* -> skip ;
// BLOCK_COMMENT : '/*' .*? '*/' -> skip ;


// /// Parser Rules (for testing purposes)

