#import <Foundation/Foundation.h>

int century(int year) {
    return year / 100 + (year % 100 > 0 ? 1 : 0);
}