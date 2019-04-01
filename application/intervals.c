#include <stdio.h>

int main(){
	int amount; // amount of numbers in input
	int temp; // variable used in sorting
	int consecutive_count; // amount of consecutive numbers in numbers[]
	int last_consecutive_number = 0; // index of the last consecutive number in numbers[]
	int first_in_interval; // first number in interval

	// input amount of numbers to work with
	printf("Enter amount of numbers: ");
	scanf("%d", &amount);
	
	int numbers[amount]; // array of input numbers

	// input the numbers & putting them in numbers[]
	for (int i = 0; i < amount; i++){
		printf("Enter number No. %d: ", i + 1);
		scanf("%d", &numbers[i]);
	}
	
	// sort the numbers of numbers[] in ascending order
	for (int i = 0; i < amount; i++){
		for (int j = i + 1; j < amount; j++){
			if (numbers[i] > numbers[j]){
				temp = numbers[i];
				numbers[i] = numbers[j];
				numbers[j] = temp;
			}
		}
	}

	printf("\nResults:\n");

	// finding intervals & output the results
	do {
		consecutive_count = 1;
		first_in_interval = numbers[last_consecutive_number];

		while (numbers[last_consecutive_number] + 1 == numbers[last_consecutive_number + 1]){
			consecutive_count++;
			last_consecutive_number++;
		}

		printf("[%d, %d] with consecutive count of %d\n", first_in_interval, numbers[last_consecutive_number], consecutive_count);

		last_consecutive_number++;
	} while (last_consecutive_number < amount);

	return 0;
}
