#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <turboc.h>
#define SPEED 20

char *shape[] = {"  ","▣","□","▧"};
int GameBoard[24][14]={ 
				{4,4,4,4,4,4,4,4,4,4,4,4,4,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
		        {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
	            {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
                {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,4,4,4,4,4,4,4,4,4,4,4,4,4}
};

int SaveBoard[24][14]={
				{4,4,4,4,4,4,4,4,4,4,4,4,4,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
		        {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
	            {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
                {4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,0,0,0,0,0,0,0,0,0,0,0,0,4},
				{4,4,4,4,4,4,4,4,4,4,4,4,4,4}
};

int bl[4][4][3][3] =      {{{{0,3,3},{0,0,3},{0,0,3}},  //ㅁㅁleft
							{{3,3,3},{3,0,0},{0,0,0}},  //  ㅁ
							{{3,0,0},{3,0,0},{3,3,0}},  //  ㅁ
							{{0,0,0},{0,0,3},{3,3,3}}},

							{{{3,3,0},{0,3,3},{0,0,0}}, //   ㅁ
							{{0,3,0},{3,3,0},{3,0,0}},  // ㅁㅁ
							{{3,3,0},{0,3,3},{0,0,0}},  // ㅁ
							{{0,3,0},{3,3,0},{3,0,0}}},

							{{{3,3,3},{0,3,0},{0,0,0}}, //ㅁㅁㅁleft
							{{3,0,0},{3,3,0},{3,0,0}},  //  ㅁ
							{{0,0,0},{0,3,0},{3,3,3}},
							{{0,0,3},{0,3,3},{0,0,3}}},

							{{{3,3,0},{3,3,0},{0,0,0}}, //ㅁㅁ
							{{3,3,0},{3,3,0},{0,0,0}},  //ㅁㅁ
							{{3,3,0},{3,3,0},{0,0,0}},
							{{3,3,0},{3,3,0},{0,0,0}}}};


int fb, sb=0, bs=0; // 블럭 종류
int xInt=0, yInt=0; //좌표값 
int xgInt = 1, ygInt = 5; // 게임보드 배열값
int line = 1;

/*void gotoxy( int x, int y )
{
	COORD XY = { x, y };
	HANDLE hHandle = GetStdHandle( STD_OUTPUT_HANDLE );
	SetConsoleCursorPosition( hHandle, XY );
} */

void BlockPrint() // 블럭을 보드에 복사
{
	int i, j;
	
	for(i=0; i<3; i++) {
		for(j=0; j<3; j++) {
			if(bl[fb][sb][i][j] == 3) 
				GameBoard[xgInt+i][ygInt+j] = bl[fb][sb][i][j];
		}
	}
}

void GameBoardPrint() // 게임보드 및 블럭  출력
{
	int i, j;
	for(i=0; i<24; i++) {
			gotoxy(xInt, yInt+i);
			for(j=0; j<14; j++) {
				if(GameBoard[i][j] == 4)
					printf("%s", shape[1]);
				else if(GameBoard[i][j] == 3)
					printf("%s", shape[2]);
				else if(GameBoard[i][j] == 5)
					printf("%s", shape[3]);
				else if(GameBoard[i][j] == 0)
					printf("%s", shape[0]);
			}
		}
}

void GameBoardReset() // 게임보드를 초기화
{
	int i, j;
	for(i=0; i<24; i++) {
		for(j=0; j<14; j++) {
			GameBoard[i][j] = SaveBoard[i][j];
			if(GameBoard[i][j] != 4 && GameBoard[i][j] != 5)
				GameBoard[i][j] = 0;
		}
	}
}

void CopyBoard() // 게임보드를 세이브보드로 복사
{
	int i, j;
	for(i=0; i<24; i++) {
		for(j=0; j<14; j++) {
			if(GameBoard[i][j] == 3)
				GameBoard[i][j] = 5;
			SaveBoard[i][j] = GameBoard[i][j];
		}
	}
	printf("Copy");
}

int MoveLEFT()  // 블럭을 왼쪽으로 이동
{	
	int i, j, go=1;
	for(i=0; i<3; i++) {
		for(j=0; j<3; j++) {
			if(GameBoard[xgInt+i][ygInt+j] == 3) {
				if(GameBoard[xgInt+i][ygInt+j-1] == 5 || GameBoard[xgInt+i][ygInt+j-1] == 4)  
					return 0;	
			}
		}
	 }

	if(ygInt > 0)
		ygInt = ygInt-1;
}

int MoveRIGHT() //블럭을 오른쪽 이동
{
	int i, j, go=1;
	for(i=0; i<3; i++) {
		for(j=0; j<3; j++) {
			if(GameBoard[xgInt+i][ygInt+j] == 3) {
				if(GameBoard[xgInt+i][ygInt+j+1] == 5 || GameBoard[xgInt+i][ygInt+j+1] == 4)  
					return 0;	
			}
		}
	 }
	if(ygInt < 13)
		ygInt = ygInt+1;
}
int MoveDOWN() // 블록 내리기
{
	int i, j;
	for(i=0; i<3; i++) {
		for(j=0; j<3; j++) {
			if(GameBoard[xgInt+i][ygInt+j] == 3) {
				if(GameBoard[xgInt+i+1][ygInt+j] == 5 || GameBoard[xgInt+i+1][ygInt+j] == 4) { 
					return 0;
				}
			}
		}
	}
	
	if(xgInt <22) {
		xgInt = xgInt+1;
		line++;
	}
}

void DownStraight() // 빠르게 내리기
{
	while(MoveDOWN() != 0)
	{
		GameBoardReset();
		BlockPrint();
	}
}

void Rotation() // 블럭 변환
{
	int i, go=1;
	sb++;
	BlockPrint();
	for(i=0; i<3; i++) {
		if(GameBoard[xgInt+i][0] == 3 || GameBoard[xgInt+i][13] == 3 || GameBoard[23][ygInt+i] == 3) {
			sb--;
			break;
		}
	 }
	if(sb == 4)
		sb = 0;
}

void Input() //  키 입력
{
	int ch;
	if(kbhit())	{
		ch = getch();
		if(ch == 224)
			ch = getch();
		switch(ch)
		{
			case 75:	
				MoveLEFT();
				break;
			case 77:
				MoveRIGHT();
				break;
			case 80:
				MoveDOWN();
				break;
			case 72:
				Rotation();
				break;
			case 32:
				DownStraight();
				break;
		}
	}
}

void LineDelete(int line)
{
	int i, j;
	for(i=1; i<=13; i++) {
		SaveBoard[line][i] = 0;
	}
	for(i=line; i>=2; i--) {
		for(j=1; j<=13; j++) {
			SaveBoard[i][j] = SaveBoard[i-1][j];
		}
	}
}
int Line()
{
	int i=1, j;
	int cnt=0;
	while(1)
	{
		for(j=1; j<=13; j++) {
				if(SaveBoard[i][j] == 5)
					cnt++;
				else if(cnt == 13)
					LineDelete(i);
		}
		if(i ==22)
			return 0;
		else {	
			cnt = 1;
			i++;
		}
	}
	return 0;
}



int main()
{
	int count = 0;
	HANDLE hConsole; // 콘솔 핸들
	CONSOLE_CURSOR_INFO ConsoleCursor; // 콘솔커서 정보 구조체
	hConsole = GetStdHandle(STD_OUTPUT_HANDLE); // 핸들을 구하고
	ConsoleCursor.bVisible = false; // true 보임 , false 안보임
	ConsoleCursor.dwSize = 1; // 커서 사이즈
	SetConsoleCursorInfo(hConsole , &ConsoleCursor); // 설정
	srand(time(NULL));
	while(1)
	{
		count++;
		BlockPrint();
		GameBoardPrint();
		delay(20);
		if(count % SPEED == 0) {
			if(MoveDOWN() == 0) {
				CopyBoard();
				Line();
				line = 1;
				xgInt=1;
				ygInt=5;
				fb = rand() %4;
				fflush(stdin);
			}
		}
		else
			Input();
		printf("%d", line);
		GameBoardReset();
	}
	return 0;
}