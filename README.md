# Weather-Forecast
"# Weather_Forecast_Prediction " Used IoT device like DHT22, BMP180 and Arduino to collect the data pertaining to the weather like temperature, humidity, pressure for three days and then use this data to run a deep learning algorithm RNN that will help us to predict the future values of these attributes for every 10 minutes to predict the type of weather that the area could experience using Zambretti algorithm.
 Weather Prediction with help of implementation of the Zambretti Algorithm.
 
 **METHODOLOGY:**
We used the sensors namely, BMP-180 which is a pressure sensor to get the pressure readings and DHT-22 which a temperature and humidity sensor to get the required data. We connected the IoT devices through appropriate wiring and hard coded the Arduino to collect the data after every 10 minutes. The Node MCU was connected to the Things board cloud service platform, where the data was getting stored and visualized. Then we used the collected data to train the algorithm for weather prediction. We used LSTM algorithm which is a type of RNN with more memory capabilities such that the previous data can be used to predict the outcome of the future occurrences. We applied this algorithm individually for the temperature, humidity, pressure values. From the predicted temperature and pressure, we also calculated the sea level pressure based on the altitude of the given surface, as in this case Vellore and its altitude 213. We used ZAMBRETTI algorithm to predict the weather based on the predictedvalues of temperature, pressure and humidity. 
