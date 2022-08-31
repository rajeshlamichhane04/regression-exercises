def scale_data(train,validate,test,columns):
    #make the scaler
    scaler = MinMaxScaler()
    #fit the scaler at train data only
    scaler.fit(train[columns])
    #tranforrm train, validate and test
    train_scaled = scaler.transform(train[columns])
    validate_scaled = scaler.transform(validate[columns])
    test_scaled = scaler.transform(test[columns])
    
    # Generate a list of the new column names with _scaled added on
    scaled_columns = [col+"_scaled" for col in columns]
    
    #concatenate with orginal train, validate and test
    scaled_train = pd.concat([train.reset_index(drop = True),pd.DataFrame(train_scaled,columns = scaled_columns)],axis = 1)
    scaled_validate = pd.concat([validate.reset_index(drop = True),pd.DataFrame(validate_scaled, columns = scaled_columns)], axis = 1)
    scaled_test= pd.concat([test.reset_index(drop = True),pd.DataFrame(test_scaled,columns = scaled_columns)],axis = 1)
    
    return scaled_train,scaled_validate,scaled_test