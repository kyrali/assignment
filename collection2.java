package collection;

import java.util.ArrayList;

public class collection2 {
	ArrayList<String>my_collection;
	int pointer;
	

	public collection2() {
		pointer=0;
		my_collection=new ArrayList<String>();
		
		
		
	}
	public void addItem(String s_to_add) {
		my_collection.add(s_to_add);
		
		
	}
	public String getNext() {
		String toreture=my_collection.get(pointer);
		pointer++;
		return toreture;
		
		
	}
	
	
	
	
    public boolean hasNext() {
    	my_collection.size();
    	if (pointer< my_collection.size()) {
    		return true;
    		
    	}
    	else {
    		return false;
    	}
    	
    }
}
