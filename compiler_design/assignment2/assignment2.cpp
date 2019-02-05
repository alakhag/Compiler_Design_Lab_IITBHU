#include<iostream>
#include<stdio.h>
#include<string.h>

#define number_of_keywords 22
#define number_of_operators 7
char keywords[][10] = {"if\0", "else\0", "while\0", "do\0", "break\0", "continue\0", "int\0", "double\0", "float\0", "return\0", "char\0", "case\0", "sizeof\0", "long\0", "short\0", "typedef\0", "switch\0", "unsigned\0", "void\0", "static\0", "struct\0", "goto\0"};
char operators[] = {'+', '-', '*', '/', '=', '>', '<'};

char buffer[1000];

using namespace std;

bool is_end(char x)
{
	if(x<'0' || (x>'9' && x<'A') || (x>'Z' && x<'a') || x>'z')
		return true;
	return false;
}

bool isvariable(char str[])
{
	if((str[0]>='0' && str[0]<='9') || is_end(str[0]))
		return false;
	return true;
}

bool is_keyword(char str[])
{
	int i;
	for(i=0; i<number_of_keywords; i++)
		if(strcmp(str, keywords[i])==0)
			return true;
	return false;
}

int string_length(char str[])
{
	int i = 0;
	while(str[i]!='\0')
		i++;
	return i;
}

int has_dot(char str[])
{
	int l = string_length(str);
	int i;
	for(i=0; i<l; i++)
		if(str[i]=='.')
			return i;
	return -1;
}

int number(char str[])
{
	int i;
	int l = string_length(str);
	if(l==0)
		return 0;
	int dot = has_dot(str);
	int flag = 0;
	for(i=0; i<l; i++)
	{
		if(i==dot)
			continue;
		if(str[i]<'0' || str[i]>'9')
		{
			if((str[i]=='-' || str[i]=='+') && i==0 && (dot>=0?l>2:l>1))
				continue;
			return 0;
		} 
	}
	if(dot==-1)
		return 1;
	else if(dot>=0)
		return 2;
}

bool is_operator(char x)
{
	int i;
	for(i=0; i<number_of_operators; i++)
		if(x==operators[i])
			return true;
	return false;
}

void parse(char str[])
{
	int left = 0, right = 0;
	int l = string_length(str);
	int j, k, num;
	while(right<l && left<=right)
	{
		if(!is_end(str[right]))
			right++;
		if(is_end(str[right]) && left==right)
		{
			if(is_operator(str[right]))
				cout<<str[right]<<" is an operator\n";
			right++;
			left = right;
		}
		else if(is_end(str[right]) && left!=right)
		{
			j = 0;
			k = left;
			while(k<right)
				buffer[j++] = str[k++];
			buffer[j] = '\0';

			num = number(buffer);
			
			if(is_keyword(buffer))
				cout<<buffer<<" is a keyword\n";
			else if(num>0)
			{
				if(num==1)
					cout<<buffer<<" is an integer\n";
				else if(num==2)
					cout<<buffer<<" is a float\n";
			}
			else if(isvariable(buffer))
				cout<<buffer<<" is a variable\n";
			else
				cout<<buffer<<" is synctactically wrong\n";
			left = right;
		}
	}
}

int main()
{
	char str[1000000];
	while(true)
	{
		cout<<"\n";
		gets(str);
		parse(str);
	}
	return 0;
}
