#include <helics/helics.hpp>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>

int main(){
    std::cout << "-------------!!!helics test: HELICS Version: " << helics::versionString << std::endl;
    std::string configFile = "/home/lei/Desktop/test-helics/federates/helics_config_2.json";
    helics::ValueFederate fed(configFile);
    helics::Publication pub;
    helics::Input sub;
    double helics_requestTime = 0.0;
    
    //to get publication definitions
    int pubCount = fed.getPublicationCount();
    
    printf("-------------helics test: num of pub: %d \n", pubCount);
    for(int i = 0; i < pubCount; i++) {
        pub = fed.getPublication(i);
        std::string pubInfo = pub.getInfo();
    }
    
    //to get subscription definitions
    int subCount = fed.getInputCount();
    printf("-------------helics test: num of sub: %d \n", subCount);
    
    for(int i = 0; i < subCount; i++) {
        sub = fed.getInput(i);
    }
    //let helics broker know you are ready to start simulation 
    fed.enterExecutingMode();

    for(int i = 0; i < pubCount; i++) {
        pub = fed.getPublication(i);
        std::string pubInfo = pub.getInfo();
        // double pub_info = 2.0;
        auto pub_info = helics::helicsGetComplex(helics::helicsComplexString(2, 2));
        pub.publish(pub_info);
    }

    // helics_requestTime = 0.05;
    double helics_grantime;
    helics_grantime = fed.requestTime(helics_requestTime);

    // double subvalue = 0.0;
    
    for(int i = 0; i < subCount; i++) {
        sub = fed.getInput(i);
        printf("-------------!!!helics debug entering  sub loop\n"); 
        // if(sub.isUpdated()) {
        auto subvalue = fed.getDouble(sub);
        // subvalue = fed.getDouble(sub);
        // printf("-------------!!!Helics sub value: %s \n", subvalue);
        std::cout << "fed 2 subvalue:  " << subvalue << std::endl;
                            //update GridPACK object property with value
        // }
    }

}