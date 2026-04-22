// 以下题目为AP CSA 24年卷的第4大题
public class TreasureMap{
	private Treasure[][] map;
	public TreasureMap(int r, int c, ArrayList<Location> locs){
		map = new int[r][c];
		for(Location loc:locs){
			int row = loc.getRow();
			int col = loc.getCol();
			map[row][col] = new Treasure();
		}
	}

	public int totalGold(Location start, Location end){
		int minRow = start.getRow();
		int minCol = start.getCol();

		int maxRow = end.getRow();
		int maxCol = end.getCol();
		
		int total = 0;
		for(int i = minRow; i <= maxRow; i++){
			for(int j = minCol; j <= maxCol; j++){
				if (map[i][j]){
					total += map[i][j].getTreasure();
					
				}
			}
		}

		return total;
	}
}
