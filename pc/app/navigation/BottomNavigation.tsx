import React, { useState } from "react";
import { BottomNavigation } from "react-native-paper";
import { useAppTheme } from "../index";
import HomeScreen from "../screens/HomeScreen";
import ProfileScreen from "../screens/ProfileScreen";
import PublishScreen from "../screens/PublishScreen";
import SearchScreen from "../screens/SearchScreen";

const BottomNavigationBar = () => {
  const {
    colors: { primary },
  } = useAppTheme();
  const [index, setIndex] = useState(0);
  const [routes] = useState([
    {
      key: "home",
      title: "Home",
      focusedIcon: "home",
    },
    { key: "search", title: "Search", focusedIcon: "magnify" },
    { key: "publish", title: "Publish", focusedIcon: "plus" },
    { key: "profile", title: "Profile", focusedIcon: "account" },
  ]);

  const renderScene = BottomNavigation.SceneMap({
    home: HomeScreen,
    search: SearchScreen,
    publish: PublishScreen, // Updated to use PublishScreen
    profile: ProfileScreen,
  });

  return (
    <BottomNavigation
      navigationState={{ index, routes }}
      onIndexChange={setIndex}
      renderScene={renderScene}
      activeColor={primary} // Use the primary color from the theme
    />
  );
};

export default BottomNavigationBar;
