from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Check for feature flag in query parameter
    feature_flag = request.args.get('feature')

    # Render new UI if feature flag is enabled
    if feature_flag == 'new-ui':
        return render_template_string("""
            <html>
                <body>
                    <div id="new-ui-banner">Welcome to the New UI!</div>
                </body>
            </html>
        """)
    else:
        # Render old UI by default
        return render_template_string("""
            <html>
                <body>
                    <div id="old-ui-banner">Welcome to the Old UI!</div>
                </body>
            </html>
        """)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)