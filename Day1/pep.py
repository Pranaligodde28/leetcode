class Solution:
    # Function to print Pattern 2
    def pattern2(self, N):
        # Loop for rows
        for i in range(N):
            # Print stars in each row
            print("* " * (i + 1))

if __name__ == "__main__":
    # Create solution object
    sol = Solution()
    # Define N
    N = 5
    # Call pattern function
    sol.pattern2(N)