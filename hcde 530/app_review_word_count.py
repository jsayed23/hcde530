def count_words(text):
    """Return the number of words in a text string."""
    return len(text.split())


reviews = [
    "Great app for tracking habits and the reminders actually help me stay consistent.",
    "The interface is clean but I wish dark mode had more customization options.",
    "I love the concept, but syncing between my phone and tablet is unreliable.",
    "Setup was quick and I could start using it in under five minutes.",
    "The latest update fixed several bugs and performance feels much faster now.",
    "Notifications are too frequent and I cannot find a way to reduce them enough.",
    "This app helps my team coordinate tasks without long email chains.",
    "Search works well, but filters are limited when I need to find older items.",
    "The onboarding tutorial was clear and made the first experience easy.",
    "I appreciate the weekly progress report because it keeps me motivated.",
    "Please add more export formats so I can share data with other tools.",
    "There are too many taps required to complete a simple action.",
    "Customer support replied quickly and solved my issue in one message.",
    "I like the color palette and typography because everything feels readable.",
    "The free version is useful, but premium pricing feels a little high.",
    "Offline mode is helpful when I am traveling without stable internet.",
    "The app crashes sometimes when I attach large images to a note.",
    "I enjoy the streak feature because it encourages daily engagement.",
    "The calendar view is confusing and dates are hard to scan quickly.",
    "Collaboration tools are strong and comments help clarify feedback.",
    "Please allow custom categories so I can organize projects my own way.",
    "I switched from another app and the import process was surprisingly smooth.",
    "Battery usage seems high after long sessions and needs optimization.",
    "The widget on my home screen is useful and updates in real time.",
    "I cannot edit old entries without opening too many menus.",
    "Voice input works better than expected and saves me a lot of time.",
    "The loading spinner appears too often even on a fast connection.",
    "I like the minimalist design and low clutter compared with competitors.",
    "Account creation was simple and login has been reliable every day.",
    "Please improve accessibility labels for screen readers across all buttons.",
    "The app is stable overall and I rarely experience unexpected errors.",
    "I would love keyboard shortcuts in the desktop version for power users.",
    "Charts are informative, but axis labels are too small to read.",
    "Sharing links with teammates is fast and permissions are easy to manage.",
    "Sometimes the app freezes for a second when switching tabs.",
    "The reminder sounds are pleasant and not distracting during work.",
    "I found a typo in settings and reported it through feedback.",
    "It took me a while to understand billing details in the subscription screen.",
    "I use this every day and it has become part of my routine.",
    "Please add bulk actions for deleting multiple items at once.",
    "The recent redesign looks modern, but contrast could be improved.",
    "Tutorial videos were helpful and answered most of my beginner questions.",
    "I like that data is backed up automatically without manual steps.",
    "The app occasionally logs me out, which interrupts my workflow.",
    "Tagging is flexible and helps me group related notes quickly.",
    "I would like a compact table view for seeing more items.",
    "Performance on older devices is acceptable but still somewhat laggy.",
    "The help center is organized well and articles are easy to follow.",
    "I appreciate the privacy controls and clear explanation of permissions.",
    "Overall this app is useful and continues to improve with each update.",
]


print(f"{'Review #':<9} {'Word Count':<10} Review Preview")
print("-" * 70)

word_counts = []

for i, review in enumerate(reviews, start=1):
    count = count_words(review)
    word_counts.append(count)

    if len(review) > 55:
        preview = review[:55] + "..."
    else:
        preview = review

    print(f"{i:<9} {count:<10} {preview}")

print("\nSummary")
print("-" * 70)
print(f"Total reviews : {len(reviews)}")
print(f"Shortest      : {min(word_counts)} words")
print(f"Longest       : {max(word_counts)} words")
print(f"Average       : {sum(word_counts) / len(word_counts):.1f} words")
