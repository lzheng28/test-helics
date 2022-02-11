#include <helics/helics.hpp>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>

int main(){
    std::cout << "-------------!!!helics test: HELICS Version: " << helics::versionString << std::endl;
    std::string configFile = "/home/lei/Desktop/test-helics/federates/helics_config_2_1.json";
    helics::ValueFederate fed(configFile);
    helics::Publication pub;
    helics::Input sub;
    double helics_requestTime = 0.0;
    double helics_grantime;
    
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

    // double pub_info = 1.0;
    std::complex<double> pub_info {1300000, 1000};
    for(int k = 0; k < 4000; k++){
        std::cout << "k: " << k << std::endl;
        for(int i = 0; i < pubCount; i++) {
            pub = fed.getPublication(i);
            std::string pubInfo = pub.getInfo();
            // pub_info += 2;
            // auto pub_info = helics::helicsGetComplex(helics::helicsComplexString(2, 2));
            // std::complex<double> pub_info {1, 1};
            pub.publish(pub_info);
        }

        helics_requestTime += 0.001;
        // helics_requestTime += 0.01;
        helics_grantime = fed.requestTime(helics_requestTime);
        std::cout << "helics_requestTime: " << helics_requestTime << std::endl;

        // double subvalue = 0.0;
        std::complex<double> subvalue {0, 0};
        for(int i = 0; i < subCount; i++) {
            sub = fed.getInput(i);
            printf("-------------!!!helics debug entering  sub loop\n"); 
            // if(sub.isUpdated()) {
            sub.getValue(subvalue);
            // subvalue = fed.getDouble(sub);
            // printf("-------------!!!Helics sub value: %s \n", subvalue);
            std::cout << "fed 2 subvalue:  " << subvalue << std::endl;
                                //update GridPACK object property with value
            // }
        }
        // helics_requestTime += 0.005;
        // // helics_requestTime += 0.01;
        // helics_grantime = fed.requestTime(helics_requestTime);
    }
}