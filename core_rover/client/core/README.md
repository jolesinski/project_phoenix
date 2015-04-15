##Client generation
Method arguments in client stubs are generated from jsonrpcstub in lexicographical order
To maintain clean api after adding new methods:  
1. generate new client  
2. git apply fixParamOrder.patch  
3. manually fix order for new methods  
4. git diff > fixParamOrder.patch
