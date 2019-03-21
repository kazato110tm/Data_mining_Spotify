
float data[][]; // Table of input data
String title[];
String artist[];
int numData; // Number of data
int numAttr; // Number of attributes of each data
float like[][];
float unlike[][];

void setup() {
  size(500,500);
  loadCSV(loadStrings ("Spotify.csv"));
  int count_l = 0;
  int count_u = 0;
  like = new float [numAttr-3][numData];
  unlike = new float [numAttr-3][numData];
  for(int i = 0; i < numData; i++){
     if(data[14][i] == 1){
       for(int j=1; j<numAttr-2; j++)
         like[j-1][count_l] = data[j][i];
       count_l++;
     }
     else{
       for(int j=1; j<numAttr-2; j++)
         unlike[j-1][count_u] = data[j][i];
       count_u++;
     }
  }
  dataNormalization (data, 0, 1);
  dataNormalization (like, 0, 1);
  dataNormalization (unlike, 0, 1);
}

void keyPressed() {
  if (key == 's')
    save("image.png");
}
