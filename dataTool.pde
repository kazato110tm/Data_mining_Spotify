
// Read and convert string arrays into numerical table
void loadCSV (String[] strs) {
  numData = strs.length - 1; // omit the first header row
  numAttr = splitTokens(strs[0], ",").length; 
  data = new float [numAttr][numData];
  title = new String [numData];
  artist = new String [numData];
  
  for (int i=0; i < numData; i++) { // Read all data items into 2D array
    String [] values = splitTokens(strs[i+1], ",");
    for (int j=0; j < numAttr-1; j++)
      data[j][i] = float(values[j]); 
    title[i] = values[numAttr-1];
    artist[i] = values[numAttr];
  }
}

// Normalize data values  
void dataNormalization (float data[][], int low, int high) {
  for (int j = 0; j < data.length - 3; j++) // omit positional values
    normalizeEachItem (data[j], low, high);
}

// Nomalize values x to low <= x <= high
void normalizeEachItem (float column[], float low, float high) {
  float fmin = min (column);
  float fmax = max (column);
  int numData = column.length;
  for (int i=0; i < numData; i++)
    column[i] = map (column[i], fmin, fmax, low, high);
}
