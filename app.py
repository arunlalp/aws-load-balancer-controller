from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    tenant_id = request.headers.get("X-Tenant-ID", "Unknown Tenant")
    if tenant_id != "valid-tenant":
        return jsonify({"error": "Invalid Tenant"}), 403
    return jsonify({"message": f"Hello, {tenant_id}!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
