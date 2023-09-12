// Codigo descargado desde la página web: https://mirpas.com
// Visita mi web para más información
const int pin[] ={9,10,11,12};
const byte numeros[10] = {0b00000000,0b00000001,0b00000010, 0b00000011, 0b00000100, 0b00000101, 0b00000110,0b00000111, 0b00001000, 0b00001001};
void setup() {
  for (int i = 0; i < 4; i++){
    pinMode(pin[i], OUTPUT);
  }
}

void loop() {
  for (int i=0; i<10; i++){
    display(i);
    delay(1000);
  }
}
void display(int number){
  byte numerodigito = numeros[number];
  for (int i=0; i<4; i++){
    int bit = bitRead(numerodigito, i);
    digitalWrite(pin[i], bit);
  }
}
