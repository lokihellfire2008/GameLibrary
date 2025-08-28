# Install the PSSQLite module if not already installed
if (-not (Get-Module -ListAvailable -Name PSSQLite)) {
    Install-Module -Name PSSQLite -Force -Scope CurrentUser
}

# Import the PSSQLite module
Import-Module PSSQLite

# Get the current user's username
$currentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name.Split('\')[1]

# Define the path to the SQLite database
$databasePath = "C:\Users\$currentUser\AppData\Local\Amazon Games\Data\Games\Sql\GameProductInfo.sqlite"
echo "Path" + $databasePath

#define new connection
$conn = New-SQLiteConnection -DataSource $databasePath
$conn

# Define the query to extract the ProductTitle,ReleaseDate,GenresJson,ProductAsin,ProductSku columns
# ProductAsin,ProductSku are used for de-duping and future edition disambiguation
$query = "
SELECT
  ProductTitle,
  ReleaseDate,
  GenresJson,
  ProductAsin,
  ProductSku
FROM DbSet
ORDER BY ProductTitle COLLATE NOCASE
"
echo "Query: " + $query
# Execute the query and store the results
$results = Invoke-SqliteQuery -Query $query -SQLiteConnection $conn

# Export the results to a CSV file
$results | Export-Csv -Path "C:\Users\$env:USERNAME\Desktop\AmazonGames.csv" -NoTypeInformation -Encoding UTF8

pause
