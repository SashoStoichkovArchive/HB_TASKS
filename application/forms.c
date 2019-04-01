#include <stdio.h>
#include <string.h>

// structure for coordinations
struct coordinations_t{
	int height;
	int width;
} coordinations;

// find coordinations of a person in the additional array
struct coordinations_t find_coordinations(int height, int width, char arr[height][width], char name){
	for (int i = 0; i < height; i++){
		for (int j = 0; j < width; j++){
			if (arr[i][j] == name){
				coordinations.height = i;
				coordinations.width = j;
				return coordinations;
			}
		}
	}

	return coordinations;
}

int main(){
	int height, width; // height and width of the cinema

	// input height and width of the cinema
	printf("Enter height and width of the cinema: ");
	scanf("%d %d", &height, &width);

	char cinema[height][width]; // 2d array of the cinema
	char result[height][width]; // result array for print

	// input the cinema layout
	printf("Enter the cinema layout:\n");
	for (int i = 0; i < height; i++)
		scanf("%s", cinema[i]);

	// input number of configurations
	int number_of_configurations;
	printf("Enter number of configurations: ");
	scanf("%d", &number_of_configurations);
	
	getchar(); // ignore __ENTER__

	// input name of the "central" person
	char central_person;
	printf("Enter the name of the central person: ");
	central_person = getchar();
	
	// input configurations
	char configurations[number_of_configurations][3];
	for (int i = 0; i < number_of_configurations; i++){
		printf("Enter configuration No. %d: ", i + 1);
		scanf("%s", configurations[i]);
	}

	printf("\n");

	int add_arr_height = height + 1;
	int add_arr_width = (width * 2) + 1;

	char array_for_configurations[add_arr_height][add_arr_width]; // additional array for configurations

	// fill the additional array with '.'
	for (int i = 0; i < (add_arr_height); i++){
		for (int j = 0; j < (add_arr_width); j++)
			array_for_configurations[i][j] = '.';
	}
	
	array_for_configurations[height][width] = central_person;

	// create configuration
	for (int i = 0; i < number_of_configurations; i++){
		find_coordinations(add_arr_height, add_arr_width, array_for_configurations, configurations[i][2]);
		
		switch(configurations[i][1]){
			case 'A':
				array_for_configurations[coordinations.height-1][coordinations.width] = configurations[i][0];
				break;
			case 'R':
				array_for_configurations[coordinations.height][coordinations.width+1] = configurations[i][0];
				break;
			case 'L':
				array_for_configurations[coordinations.height][coordinations.width-1] = configurations[i][0];
				break;
		}
	}

	int up_index = 0;
	int left_index = 0;
	int right_index = 0;

	// find up_index
	for (int i = 0; i < add_arr_height; i++){
		for (int j = 0; j < add_arr_width; j++){
			if (array_for_configurations[i][j] != '.'){
				up_index = i;
				break;
			}
		}

		if (up_index != 0) break;
	}

	// find left_index
	for (int i = 0; i < add_arr_width; i++){
		for (int j = 0; j < add_arr_height; j++){
			if (array_for_configurations[j][i] != '.'){
				left_index = i;
				break;
			}
		}

		if (left_index != 0) break;
	}

	// find right_index
	for (int i = add_arr_width - 1; i > 0; i--){
		for (int j = 0; j < add_arr_height; j++){
			if (array_for_configurations[j][i] != '.'){
				right_index = i;
				break;
			}
		}

		if (right_index != 0) break;
	}

	int h, w, h_config, w_config;
	int counter = 0;

	// find possibilities and printing them
	for (int i = 0; i < (height - (add_arr_height - up_index) + 1); i++){
		for (int j = 0; j < (width - (right_index - left_index + 1) + 1); j++){
			h = i; w = j;
			h_config = up_index; w_config = left_index;

			for (int a = 0; a < height; a++){
				for (int b = 0; b < width; b++)
					result[a][b] = cinema[a][b];
			}

			while ((array_for_configurations[h_config][w_config] != '.' && cinema[h][w] == '.') || 
				   (array_for_configurations[h_config][w_config] == '.' && cinema[h][w] == '.') ||
				   (array_for_configurations[h_config][w_config] == '.' && cinema[h][w] == '*')	  ){

				if (array_for_configurations[h_config][w_config] != '.')
					result[h][w] = array_for_configurations[h_config][w_config];

				w++; w_config++;

				if (w > (right_index - left_index + j)){
					h++; h_config++;
					w = j; w_config = left_index;
				}

				if (h > (add_arr_height - up_index - 1 + i)){
					counter++;

					printf(" ");
					for (int a = 0; a < width; a++) printf("%d", a);
					printf("\n");

					for (int a = 0; a < height; a++){
						printf("%d", a);
						for (int b = 0; b < width; b++)
							printf("%c", result[a][b]);
						printf("\n");
					}
					
					for (int a = 0; a < (width + 1); a++) printf("-");
					printf("\n");

					break;
				}
			}
		}
	}

	printf("Number of possible configurations: %d\n", counter);

	return 0;
}
