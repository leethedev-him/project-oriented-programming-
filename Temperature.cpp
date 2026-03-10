/*
F = (C * 9/5) + 32
C = (F - 32) * 5/9

30c => 86f

*/

#include <iostream>
using namespace std;


char to_lower(char n);

void caller(){
    for (int i = 1; i< 300; i++)
        cout << i << (char) i << '\n';
}


double toFheit(double celcius);

double toCelcius(double fheit);

int main(){
    
    cout << "!============== Temperature Converter in C++ ===============!\n";
    
    double source;
    cout << "Enter the value you want to convert from: ";
    cin >> source;

    char dest;
    cout << "Enter the unit you want to convert to: ";
    cin >> dest;

    dest = to_lower(dest);

    if (!(dest == 'f' || dest == 'c'))
        cout << "Enter either 'f' or 'c' only, please try again!\n";
    else if (dest == 'c')
        cout << source << " to Celcius is " << toCelcius(source) <<  'C';
    else
        cout << source << " to Fahrenheit is " << toFheit(source) << 'F';
    
     
    return 0;
}
// ℃℉

char to_lower(char n){
    if (n > 64 && n < 92)
        return (n + 32);
    else
        return n;
}


double toFheit(double celcius){
    return (celcius * 9/5.0) + 32;
}

double toCelcius(double fheit){
    return (fheit - 32) * 5/9.0;
}

