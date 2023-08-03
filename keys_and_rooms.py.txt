class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		n = len(rooms)
		visited = [False]*n
		visited[0] = True

		def dfs(room):
			nonlocal visited
			if visited[room]:
				keys = rooms[room]
				for key in keys:
					if not visited[key]:
						visited[key] = True
						dfs(key)
		return
	
		dfs(0)
		return reduce(lambda x, y: x and y, visited)