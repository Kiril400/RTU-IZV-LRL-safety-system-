/*
#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>
#include <sha/sha256.h>

/*

When uploading code, use UART(ESP32S3 specific)



PIN ON ESP8266 - PIN ON RC522

10 - NSS(Chip select)
11 - MOSI(Master out slave in)
12 - SCK(Serial clock)
13 - MISO(Master in slave out)
GND - GND
3V3 - VCC

Leave RST and IRQ unconnected

* /

#define SS_PIN 10 // Chip select
#define RST_PIN 9 // Redundant
 
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of reader
MFRC522::MIFARE_Key defaultkey; // Create default key for reader (FFFFFFFFFFFF)

void setup() { 
  Serial.begin(115200); // Init Serial
  SPI.begin(); // Init SPI bus
  rfid.PCD_Init(); // Init reader
  delay(4);
  for(byte i = 0; i < 6; i++) // Set default key
  {
    defaultkey.keyByte[i] = 0xFF;
  }
  rfid.PCD_DumpVersionToSerial();
}
 
byte lastid[10];

long long millisnow = 0;

byte buffer[18];

void loop() {
  rfid.PCD_StopCrypto1();
  if(!rfid.PICC_IsNewCardPresent())
  {
    return;
  }
  if(!rfid.PICC_ReadCardSerial())
  {
    return;
  }
  if(millis() - millisnow < 1500)
  {
    Serial.println("Chip scanned too soon");
    return;
  }
  millisnow = millis();
  Serial.println("Chip scanned");
  rfid.PICC_DumpToSerial(&(rfid.uid));
  /*
  byte buffersize = sizeof(buffer);
  MFRC522::StatusCode status = rfid.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, 0x00, &(defaultkey), &(rfid.uid));
  if(status != MFRC522::STATUS_OK)
  {
    Serial.println("Authenticate failed.");
    Serial.println(MFRC522::GetStatusCodeName(status));
    return;
  }
  rfid.MIFARE_Read(0x00, buffer, &(buffersize));
  for(byte i = 0; i < buffersize; i++)
  {
    Serial.print(buffer[i], HEX);
    Serial.print(" ");
  }
  Serial.println();
  * /
}
*/