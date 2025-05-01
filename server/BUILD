load("@rules_rust//rust:defs.bzl", "rust_binary")

rust_binary(
    name = "server",
    srcs = ["src/main.rs"],
    edition = "2024",
    deps = [
        # External crates
        "@crates//:rumqttd",
        "@crates//:tracing-subscriber",
        "@crates//:config",
    ],
)