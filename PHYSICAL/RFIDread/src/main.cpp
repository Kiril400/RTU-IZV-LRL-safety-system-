#include <Arduino.h>
#include <SPI.h>
#include <MFRC522.h>
#include <sha/sha256.h>
#include <WiFi.h>
#include <WiFiUDP.h>

/*

When uploading code, use UART(ESP32-S3 specific)



PIN ON ESP8266 - PIN ON RC522

10 - NSS(Chip select)
11 - MOSI(Master out slave in)
12 - SCK(Serial clock)
13 - MISO(Master in slave out)
GND - GND
3V3 - VCC

Leave RST and IRQ unconnected

*/
#define SS_PIN 10 // Chip select
#define RST_PIN 9 // Redundant

/*

Set WiFi ssid and password

*/

const char* ssid = "IZV";
const char* password = "@skola12";

WiFiUDP UDP;
unsigned int port = 34623;  // local port to listen on

char incoming[255];  // buffer for incoming packets
char sendpacket[10];

 
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of reader
MFRC522::MIFARE_Key defaultkey; // Create default key for reader (FFFFFFFFFFFF)

void setup() { 
    Serial.begin(115200); // Init Serial
    SPI.begin(); // Init SPI bus
    rfid.PCD_Init(); // Init reader
    delay(10);
    rfid.PCD_DumpVersionToSerial();

    Serial.printf("Connecting to %s ", ssid);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println(" connected");

    UDP.begin(port);
    Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), port);
    delay(3000);
    if (rfid.PCD_PerformSelfTest())
    {
        Serial.println("Passed Self-Test");
    }
}
 
byte lastid[10];

long long millisnow = 0;

byte buffer[18];

void loop() {
    if(UDP.parsePacket())
    {
        int len = UDP.read(incoming, 255);
        incoming[len] = 0;
        for(int i = 0; i < len; i++)
        {
            Serial.print(incoming[i], HEX);
        }
    }
    if(millis() - millisnow < 1500)
    {
        return;
    }
    if(!rfid.PICC_IsNewCardPresent())
    {
        Serial.println("No card detected");
        return;
    }
    if(!rfid.PICC_ReadCardSerial())
    {
        Serial.println("Cant read UID");
        return;
    }
    millisnow = millis();
    Serial.println("Chip scanned");
    for(int i = 0; i < rfid.uid.size; i++)
    {
        Serial.print(rfid.uid.uidByte[i], HEX);
        Serial.print(" ");
    }
    for(int i = 0; i < rfid.uid.size; i++)
    {
        sendpacket[i] = (char)rfid.uid.uidByte[i];
    }
    for(int i = rfid.uid.size; i < 10; i++)
    {
        sendpacket[i] = 0;
    }
    //Change to IP and port of target server
    UDP.beginPacket("10.109.6.206", 35682);
    UDP.print(sendpacket);
    UDP.endPacket();
    Serial.println();
}