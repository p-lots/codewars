#import <Foundation/Foundation.h>
NSString* evenOrOdd (NSInteger n)
{
    return n % 2 == 0 ? @"Even" : @"Odd";
}