#include <iostream>

#include "roverclient.h"
#include <jsonrpccpp/client/connectors/httpclient.h>


using namespace jsonrpc;
using namespace std;

int main()
{
    HttpClient httpclient("http://localhost:8383");
    RoverClient client(httpclient);
    try
    {
        cout << client.setJointAngle(3.14, 1) << endl;
    }
    catch (JsonRpcException e)
    {
        cerr << e.what() << endl;
    }
}