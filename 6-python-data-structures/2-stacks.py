# Stacks: LIFO Data Structure
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
browsing_session.append(4)
print(browsing_session)
# Remove top item
browsing_session.pop()
print(browsing_session)

# Get top item, first check stack isn't empty
# Otherwise if empty we would get error
# Remember empty lists are falsy
if browsing_session:
    print(browsing_session[-1])
