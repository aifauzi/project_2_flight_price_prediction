# Prediction of Flight Price
![Flight](https://github.com/aifauzi/project_2_flight_price_prediction/blob/main/deployment/flight_ticket_prices.jpeg)

## Case Background
In this *project*, I take the perspective of a *Data Scientist* who is asked to create a model that predicts the price of an airplane ticket for a customer who uses flight transportation. I hope this prediction model will be able to give him an idea of ​​the money he needs to prepare when he wants to travel by plane. For sure, I also to used <u>Hyperparameter Tunning</u> to search the best hyperparameter I can choose. Last but not least, I create some deployment application with <u>Streamlit</u> and store to <u>HuggingFace</u> so the customer or user can use this app and see how it works.

## Workflow
- Exploratory the dataset (understanding the meaning of each columns, check data type, etc)
- Feature Engineering (split data, feature creation, handling missing value, outlier, scaling, encoding, etc)
- Model Definition (define the model)
- Model Training (train the data with model)
- Model Evaluation (evaluate the result of model)
- Conclusion & Deployment

## Challenges
- The dataset is too much so I decided to used the sample with Slovin method.
- Some columns contain more than one value in each row and separated by the (`||`) sign. To solve that, I extracted the information that could be taken from the column, although not all of it.

## Result
The algorithm I used as a test with default parameters were *LinearRegression*, *Lasso*, *Ridge*, *ElasticNet*, *KNeighborsRegressor*, *SVR*, *DecisionTreeRegressor* and *RandomForestRegressor*. Then I choose the best model based on *cross_val_score* assessment with *scoring* **RMSE**. Also, I applied *Hyperparameter Tunning*. The smallest **RMSE** score was found in the *Ridge* model. After doing *Hyperparameter Tunning*, I got the result **RMSE** score was 1.18 but as an alternative **MAE** score I get was around 0.7 - 0.8. It's means that the model built is able to predict ticket prices with an average difference of around 1 dollar ($1) from the original price.
