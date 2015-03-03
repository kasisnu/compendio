// Recognize text on an image using Tesseract API and print it to the screen
// Usage: ./tess image.png

#include <tesseract/baseapi.h>
#include <tesseract/strngs.h>
#include <iostream>
#include <fstream>
#include <string>
#define FILE_NAME "fout.html"

int main(int argc, char** argv)
{
    std::cout << "In main.";
    if (argc != 2)
    {
        std::cout << "Please specify the input image!" << std::endl;
        return -1;
    }

    const char* lang = "eng";
    const char* filename = argv[1];

    tesseract::TessBaseAPI tess;
    tess.Init(NULL, lang, tesseract::OEM_DEFAULT);
    //tess.SetPageSegMode(tesseract::PSM_SINGLE_BLOCK);

    FILE* fin = fopen(filename, "rb");
    if (fin == NULL)
    {
        std::cout << "Cannot open " << filename << std::endl;
        return -1;
    }
    fclose(fin);

    STRING text;
    if (!tess.ProcessPages(filename, NULL, 0, &text))
    {
        std::cout << "Error during processing." << std::endl;
        return -1;
    }
    else
    //    std::cout << text.string() << std::endl;
    {
        std::cout << "In else.";
        std::ofstream fout(FILE_NAME);
        if(fout.is_open())
        {
            fout << "<html>";
            int flag = 1;
            std::string str=text.string();
            //iterate through the output string
            for(int i=0;str[i]!='\0';i++)
            {
                //check for new paragraphs
                if(str[i]=='\n'&&str[i+1]=='\n')
                {
                    str=str.replace(i,2,(flag?"<p>":"</p>"));
                    flag = (flag?0:1);                          //toggle flag
                }
                else if(str[i]=='\n')
                    str=str.replace(i,1," ");
            }
            fout << str;
            fout << "</html>";
            fout.close();
            std::cout << "File successfully created.";
        }
        else
        {
            std::cout << "Unable to open file.";
            return -1;
        }
    }
    return 0;
}