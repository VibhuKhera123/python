

# # Function to connect to Hive in a Docker container
# def connect_to_hive_docker(host='localhost', port=10000, username='hive'):
#     transport = TSocket.TSocket(host, port)
#     transport = TTransport.TBufferedTransport(transport)
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)
#     client = hive.Connection(host=host, port=port, username=username)
#     transport.open()
#     return client

# # Function to execute a Hive query
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     cursor.execute(query)
#     return cursor.fetchall()

# # Example query to get data from the flights table
# def get_flight_data(connection):
#     query = "SELECT * FROM flights LIMIT 10"
#     return execute_query(connection, query)

# # Example query to analyze search terms
# def analyze_search_terms(connection):
#     query = "SELECT searchterms, COUNT(*) AS search_count FROM flights GROUP BY searchTerms ORDER BY search_count DESC LIMIT 10"
#     return execute_query(connection, query)

# # Example query to analyze rankings
# def analyze_rankings(connection):
#     query = "SELECT title, rank FROM flights WHERE rank < 10 AND rank IS NOT NULL ORDER BY rank"
#     return execute_query(connection, query)

# def analyze_total_results(connection):
#     query = "SELECT searchterms, totalresults FROM flights WHERE totalresults > 1000 AND totalresults IS NOT NULL ORDER BY totalresults DESC LIMIT 10"
#     return execute_query(connection, query)


# # Main function
# def main():
#     # Connect to Hive
#     connection = connect_to_hive_docker()

#     # Example queries
#     flight_data = get_flight_data(connection)
#     search_terms_analysis = analyze_search_terms(connection)
#     rankings_analysis = analyze_rankings(connection)
#     total_results_analysis = analyze_total_results(connection)

#     # Print results
#     print("Flight Data:")
#     for result in flight_data:
#         print(result)

#     print("\nSearch Terms Analysis:")
#     for result in search_terms_analysis:
#         print(result)

#     print("\nRankings Analysis:")
#     for result in rankings_analysis:
#         print(result)

#     print("\nTotal Results Analysis:")
#     for result in total_results_analysis:
#         print(result)

#     # Close the connection
#     connection.close()

# if __name__ == "__main__":
#     main()

from pyhive import hive
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import sys
def connect_to_hive_docker(host='localhost', port=10000, username='hive'):
    try:
        transport = TSocket.TSocket(host, port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = hive.Connection(host=host, port=port, username=username)
        transport.open()
        return client
    except Exception as e:
        print(f"Error connecting to Hive: {e}")
        sys.exit(1)
def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return None
def get_user_input(prompt):
    return input(prompt).strip()
def main():
    connection = connect_to_hive_docker()
    while True:
        query = get_user_input("Enter your query (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        result = execute_query(connection, query)
        if result is not None:
            for row in result:
                print(row)
    connection.close()

if __name__ == "__main__":
    main()
