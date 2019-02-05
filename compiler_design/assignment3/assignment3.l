%{
	#include<stdio.h>
	int count=0;
%}

letter [a-zA-Z]
digit [0-9]
number {digit}+
variable {letter}({digit}*{letter}*)
novar {digit}({digit}*{letter}*)


%%
[\t\n";" ]+
("if")|("else")|("while")|("do")|("break")|("void")|("int")|("double")|("float")|("return")|("char")|("switch")|("case")|("sizeof")|("typedef")|("for")|("cout")|("cin")|("struct")|("goto") {printf("%s is a keyword\n", yytext);}
("+"|"-"|"*"|"/"|">"|"<"|"=") {printf("%s is operator\n", yytext);}
{number} {printf("%s is a number\n", yytext);}
{variable} {printf("%s is a variable\n", yytext); count++;}
{novar} {printf("%s is syntactically wrong\n", yytext);}
%%

int main()
{
	FILE *fp;
	char file[10];
	printf("\nEnter the filename: ");
	scanf("%s", file);
	fp=fopen(file,"r");
	yyin=fp;
	yylex();
	printf("Total identifiers are: %d\n", count);
	return 0;
}
