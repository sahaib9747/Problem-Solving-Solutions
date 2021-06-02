#include <stdio.h>
//Problem 1047
int main()
{
    int sHour,sMinute,eHour,eMinute,fHour = 24,fMinute = 0;
    scanf("%d %d %d %d",&sHour,&sMinute,&eHour,&eMinute);
    // a = sHour, b = sMinute, c = eHour, d= eMinutes
    if(sMinute < eMinute)
    {
        fMinute = eMinute - sMinute;
        fHour = 0;
        if(eHour > sHour)
        {
            fHour = eHour - sHour;
        }
        else if(sHour>eHour)
        {
            fHour = (eHour + 24) - sHour;
        }
    }
    else if(sMinute > eMinute)
        {
            fMinute = (eMinute + 60) - sMinute ;
            if(sHour == eHour)
            {
                fHour = 24 - 1;
            }
            else if(eHour > sHour)
            {
                fHour = eHour - sHour - 1;
            }
            else if(sHour>eHour)
            {
                fHour = ((eHour + 24) - sHour) - 1;
            }
        }
    if (fHour > 23 && fMinute > 0)
    {
        printf("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)\n",fMinute);
    }
    else
    {
        printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", fHour, fMinute);
    }
    return 0;
}