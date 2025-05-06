load("@rules_rust//rust:defs.bzl", "rust_binary")

rust_binary(
    name = "client_async",
    srcs = ["src/main.rs"],
    edition = "2024",
    deps = [
        # External crates
        "@crates//:rumqttc",
        "@crates//:pretty_env_logger",
        "@crates//:tokio",
    ],
)
