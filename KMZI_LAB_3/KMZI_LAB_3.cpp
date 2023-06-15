// A program to find the GCD of two numbers using command line arguments
#include <iostream>
#include <cstdlib> // for std::atoi function
#include <cmath>

// A function to return the GCD of two numbers using Euclid's algorithm
int gcd(int a, int b)
{
    // If one of the numbers is zero, the other is the GCD
    if (a == 0)
        return b;
    if (b == 0)
        return a;

    // If both numbers are equal, either one is the GCD
    if (a == b)
        return a;

    // If one number is greater than the other, subtract the smaller from the larger and repeat
    return a > b ? gcd(a - b, b) : gcd(a, b - a);
}

// A function to check if a number is prime or not
bool is_prime(int n)
{
    // If the number is less than 2, it is not prime
    if (n < 2) {
        return false;
    }

    // If the number is divisible by any number from 2 to its square root, it is not prime
    for (int i = 2; i * i <= n; i++)
    {
        if (n % i == 0)
            return false;
    }

    // Otherwise, the number is prime
    return true;
}

// A function to print all the prime numbers in a given range
int print_primes(int low, int high)
{
    int count = 0;
    // Loop through the range and check each number for primality
    for (int n = low; n <= high; n++)
    {
        if (is_prime(n))
        {
            // If the number is prime, print it
            std::cout << n << " ";
            count++;
        }
    }
    std::cout << "\nCount of prime numbers = " << count << "\n";
    std::cout << "n/ln(n) = " << high/log(high) << "\n";
    return count;
}

int main(int argc, char *argv[])
{
    int task = 0;
    int num1 = 0;
    int num2 = 0;
    int num3 = 0;
    int result = 0;

    while (true)
    {
        std::cout << "\n1 - GCD(a, b)\n";
        std::cout << "2 - GCD(a, b, c)\n";
        std::cout << "3 - primes(n, m)\n";
        std::cout << "0 - exit\n";

        scanf("%d", &task);

        switch (task)
        {
        case 0:
            return 0;
            break;
        case 1:
            std::cout << "Enter two numbers:\n";
            scanf("%d", &num1);
            scanf("%d", &num2);
            result = gcd(num1, num2);
            std::cout << "The GCD of " << num1 << " and " << num2 << " is " << result << "\n";
            break;
        case 2:
            std::cout << "Enter three numbers:\n";
            scanf("%d", &num1);
            scanf("%d", &num2);
            scanf("%d", &num3);
            result = gcd(gcd(num1, num2), num3);
            std::cout << "The GCD of " << num1 << " and " << num2 << " and " << num3 << " is " << result << "\n";
            break;
        case 3:
            std::cout << "Enter two numbers:\n";
            scanf("%d", &num1);
            scanf("%d", &num2);
            print_primes(num1, num2);
            break;

        default:
            break;
        }
    }

    return 0;
}