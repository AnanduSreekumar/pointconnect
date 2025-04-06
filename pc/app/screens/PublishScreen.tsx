import React from "react";
import { StyleSheet, Text, View } from "react-native";

const PublishScreen = () => (
  <View style={styles.container}>
    <Text>Publish Screen</Text>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

export default PublishScreen;
