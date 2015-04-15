##Client generation
Method arguments in client stubs are generated from jsonrpcstub in lexicographical order  
To maintain clean api after adding new methods:  
1. generate new client  
2. cp roverclient.h temp_roverclient.h  
3. git apply fixParamOrder.patch  
4. manually fix order for new methods  
5. git diff temp_roverclient.h roverclient.h > fixParamOrder.patch  
6. rm temp_roverclient.h
