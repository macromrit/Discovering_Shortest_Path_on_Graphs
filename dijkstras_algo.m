function distance = dijkstras_algo(map, startingpoint)
    %map of distances among N nodes
    %N = No. of nodes
    N = length(map);
    disp(N)
    %initialize the distance to all points as infinity 
    %its Inf as Nodes aren't explored yet
    distance(1:N) = Inf;
    
    %note all nodes as unvisited
    visited(1:N) = 0;
    
    %initialize the distance to the first point as zero.
    %cuz... distance from the node to itself is Nothing a.k.a 0
    distance(startingpoint) = 0;
    
    while sum(visited)<N
        %find unvisited nodes
        %anything that's visited is Inf else it stands with real weight
        candidates(1:N) = Inf;
        for index = 1:N
            if visited(index) == 0
                candidates(index) = distance(index);
            end
        end 
        
        %find the one with smallest distance value
        [currentdistance, currentnode] = min(candidates);

        %given the distance to the current point, update the distances
        %to all its neighbours if the new distance will be smaller
        for index = 1:N
            newdistance = currentdistance + map(currentnode, index);
            if newdistance < distance(index)
                distance(index) = newdistance;
            end
        end

    %mark the current node as visited
    visited(currentnode) = 1;
    

    %loop it through untill all nodes are *visited*
    end

end