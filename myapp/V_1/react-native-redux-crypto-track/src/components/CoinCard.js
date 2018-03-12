import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  Image
} from 'react-native';
import { images } from '../Utils/CoinIcons';

const styles = StyleSheet.create({
  container: {
    display: "flex"
  },
  image: {
    width: 40,
    height: 40,
  },
  bold: {
    fontWeight: 'bold'
  }
})

const { container, image, bold } = styles;

const CoinCard = ({ symbol, coin_name, price_usd, percent_change_24h, percent_change_7d }) => {
  return (
    <View>
      <Image
        style={styles.image}
        source={{ uri: images[symbol] }}
      />
      <Text>{symbol}</Text>
      <Text>{price_usd}</Text>
      <Text>{percent_change_24h}</Text>
    </View>

  )
}

export default CoinCard;