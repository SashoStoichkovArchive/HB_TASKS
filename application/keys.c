#include <stdio.h>
#include <string.h>

struct key_value_t{
	char key[32];
	int value;
};

// check if a key is in final array
int is_in_array(int number_of_lines, char key[], struct key_value_t kv_arr_final[]){
	for (int i = 0; i < number_of_lines; i++){
		if (strcmp(kv_arr_final[i].key, key) == 0) return 1;
	}

	return 0;
}

// sort structures in final array by value in descending order
void sort_values(struct key_value_t kv_arr_final[], int index){
	struct key_value_t temp;
    
    for (int i = 0; i < index - 1; i++){
		for (int j = 0; j < (index - i - 1); j++){
    		if (kv_arr_final[j].value < kv_arr_final[j + 1].value){
				temp = kv_arr_final[j];
				kv_arr_final[j] = kv_arr_final[j + 1];
				kv_arr_final[j + 1] = temp;
			}
		}
	}
}

// sort keys with equal values in alphabetical order
void sort_keys_with_equal_values(struct key_value_t kv_arr_final[], int s_value, int e_value){
	char temp[32];
	
	for (int i = s_value; i < e_value; i++) {
		for (int j = i + 1; j < e_value; j++){
			if (strcmp(kv_arr_final[i].key, kv_arr_final[j].key) > 0){
				strcpy(temp, kv_arr_final[i].key); 
				strcpy(kv_arr_final[i].key, kv_arr_final[j].key); 
				strcpy(kv_arr_final[j].key, temp); 
			}
		}
	}
}

int main(){
	struct key_value_t kv;

	// input number of lines
	int number_of_lines;
	printf("Enter number of lines: ");
	scanf("%d", &number_of_lines);

	struct key_value_t kv_arr[number_of_lines];

	printf("Enter %d lines with {key} {value}\n", number_of_lines);

	// input keys with their values
	for (int i = 0; i < number_of_lines; i++){
		printf("Enter line No %d: ", i + 1);
		scanf("%s %d", kv.key, &kv.value);
		strcpy(kv_arr[i].key, kv.key);
		kv_arr[i].value = kv.value;
	}

	struct key_value_t kv_arr_final[number_of_lines]; // non-repeatable keys with summed values in array

	int index = 0;

	// fill kv_arr_final[] with non-repeatable keys with their summed values
	for (int i = 0; i < number_of_lines; i++){
		int summed_value = 0;
		
		if (is_in_array(number_of_lines, kv_arr[i].key, kv_arr_final) == 0){
			strcpy(kv_arr_final[index].key, kv_arr[i].key);

			for (int j = i; j < number_of_lines; j++){
				if (strcmp(kv_arr_final[index].key, kv_arr[j].key) == 0) summed_value += kv_arr[j].value;
			}
			
			kv_arr_final[index].value = summed_value;
			index++;
		}
	}

	// call sort_values();
	sort_values(kv_arr_final, index);
	
	int counter = 0;
	int s_value; // start index for keys with equal values
	int e_value; // end index for keys with equal values

	printf("\nResults:\n");
	
	// output top3 values
	for (int i = 0; i < 3; i++){
		if (kv_arr_final[counter].value == kv_arr_final[counter + 1].value){
			s_value = counter;

			while (kv_arr_final[counter].value == kv_arr_final[counter + 1].value){
				counter++;
			}

			e_value = counter;
		
			sort_keys_with_equal_values(kv_arr_final, s_value, e_value + 1);
			
			for (int j = s_value; j < e_value; j++)	printf("%s, ", kv_arr_final[j].key);
			
			printf("%s: %d\n", kv_arr_final[e_value].key, kv_arr_final[counter].value);
			counter++;
		}
		
		else {
			printf("%s: %d\n", kv_arr_final[counter].key, kv_arr_final[counter].value);
			counter++;
		}

		if (counter >= index) break;
	}

	return 0;
}

