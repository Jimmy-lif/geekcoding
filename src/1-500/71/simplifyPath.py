class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/');
        canoPath = [];
        j = 0;
        for i in range(len(paths)):
            p = paths[i];
            if p == '..':
                if len(canoPath) > 0:
                    canoPath.pop(len(canoPath)-1);
            elif p == '.' or p=='/':
                continue;
            else:
                if len(p) > 0:
                    canoPath.append(p);

        result = '';
        for p in canoPath:
            result +="/";
            result +=p;
        if len(result) == 0:
            result = '/';
        return result;
