class Stack { // default capacity = 10
	private:
	int N = 0;
	int cnt = 0;
	int * arr;
	
	public:
    Stack() {
        N = 10;
        arr = new int[N];
    }
    Stack(int s) {
        N = s;
        arr = new int[N];
    }
    void push(int item) {
        arr[cnt++] = item;
    }
    StackElement pop() {
        return arr[--cnt];
    }
    bool isEmpty() {
        return cnt == 0;
    }
    bool isFull() {
        return N == cnt;;
    }
}; 
