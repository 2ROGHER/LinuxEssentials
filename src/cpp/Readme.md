## Errores (bug)
Los erros en el `codigo` son tambien conocidos como `bugs`.
- `Debugging`  o `Depuracion` es el  arte de `encontrar` y `corregir` los errores en el codigo. 
## 1. Encabezado del programa 
- Esta parte del programa es el que contiene las `funciones` y `comandos`.
- `<iostrem>`: Contiene todas las funcionalidades para trabajar con el flujo de salida y entrada del programa.
- `#include`: Es el comando que se usa para anidadir encabezados al programa.
- `namespace`: Es el comando que organiza las palabras en grupos logicos y les da nombres para que <iostream> pueda trabajar con ellos.
- `int main() {}`: Este es el punto de entrada o en punto de partida del programa en .cpp
- `endl`: Este comando  es usado para crear otra salida de linea.

```cpp
    #include <iostream>;
    using namespace std;

    int main() {
        cout << "Hello world" << endl;
        // Other code line
        cout << "This is other code line" << endl;
    }
 
```