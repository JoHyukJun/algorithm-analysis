//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


#include <iostream>
#include <queue>

#define MAX 1000001

using namespace std;

int f, s, g, u, d;
int visited[MAX] = { 0, };
queue<pair<int, int>> q;
int location, num;


bool bfs(int destination) {
	bool output = false;

	while (!q.empty()) {
		location = q.front().first;
		num = q.front().second;
		q.pop();

		if (location == destination) {
			output = true;
			return output;
		}

		if (location + u <= f && visited[location + u] == 0) {
			q.push(make_pair(location + u, num + 1));
			visited[location + u] = 1;
		}
		if (location - d > 0 && visited[location - d] == 0) {
			q.push(make_pair(location - d, num + 1));
			visited[location - d] = 1;
		}
	}
	
	return output;
}


int main() {
	// faster better
    cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> f >> s >> g >> u >> d;

	q.push(make_pair(s, 0));
	visited[s] = 1;

	if (bfs(g)) {
		cout << num;
	}
	else {
		cout << "use the stairs";
	}
	
	return 0;
}