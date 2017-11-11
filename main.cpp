#include <stdio.h>
#include <iostream>
#include "SDL2/SDL.h"
#include "SDL2_ttf/SDL_ttf.h"
#include <thread>
#include <vector>
#include <fstream>//read & write files
#include <dirent.h>
#include <assert.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    bool success = true;
    //just gonna pull my fonts from Heptarchy Cocoa instead of setting them up in this project's folders
    std::string dumstupidcurrentdirectorybs = "/Users/baileyandrew/Desktop/Heptarchy Cocoa/";
    if( !init() ) {
        printf( "Failed to initialize!\n" );
    }
    else {
        //get screen resolution:
        SCREEN_WIDTH = 400;
        SCREEN_HEIGHT = 400;
        SDL_SetWindowPosition(gWindow, 300, 300);
        SDL_SetWindowSize(gWindow, SCREEN_WIDTH, SCREEN_HEIGHT);

        if( TTF_Init() == -1 ) {
            printf( "SDL_ttf could not initialize! SDL_ttf Error: %s\n", TTF_GetError() );
            //success = false;
            throw std::runtime_error("Font renderer could not be initialized!");
        }
        //init font
        theFont24 = TTF_OpenFont((dumstupidcurrentdirectorybs+"resources/Fonts/Times New Roman.ttf").c_str(),24);
        //std::cout << SDL_GetError();
        theFont20 = TTF_OpenFont((dumstupidcurrentdirectorybs+"resources/Fonts/Times New Roman.ttf").c_str(),20);
        theFont16 = TTF_OpenFont((dumstupidcurrentdirectorybs+"resources/Fonts/Times New Roman.ttf").c_str(),16);
        if (!theFont24||!theFont20||!theFont16) {
            printf("Failed to load fonts!");
            throw std::runtime_error("Failed to load fonts! - had checked directory "+dumstupidcurrentdirectorybs);
        }
        //Create vsynced renderer for window
        if( gRenderer == NULL ) {
            printf( "Renderer could not be created! SDL Error: %s\n", SDL_GetError() );
            success=false;
        }
        else {
            //Initialize renderer color
            SDL_SetRenderDrawColor( gRenderer, 0xFF, 0xFF, 0xFF, 0xFF );
            SDL_SetRenderDrawBlendMode(gRenderer,SDL_BLENDMODE_BLEND);

            if (success) {
                run();
            }
        }
    }
    close();
    return 0;
}
