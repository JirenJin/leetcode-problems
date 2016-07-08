class Solution {
public:
    bool isPerfectSquare(int num) {
        if (num < 1)
            return false;
        if (num == 1)
            return true;
        int start = 1;
        int end = num;
        int half = (end - start) / 2;
        while (half > 0){
            // use long here is to avoid out-of-range
            long long pivot = start + half;
            if (pivot * pivot == num)
                return true;
            else if (pivot * pivot < num)
                start = pivot;
            else
                end = pivot;
            half = (end - start) / 2;
        }
        return false;
    }
};
