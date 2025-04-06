import React from "react";
import { StyleSheet, Text, View } from "react-native";

const SearchScreen = () => (
  <View style={styles.container}>
    <Text>Search Screen</Text>
  </View>
);

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
});

export default SearchScreen;
